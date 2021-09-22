from flask import Flask,jsonify,request
from data import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "planetdata":data ,
        "message":"sucessesful",
    })
@app.route("/planet")
def planet():
    name = request . args.get("name")
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "planetdata": planet_data,
        "message": "sucess"
    })


if __name__ == "__main__":
    app.run(debug=True)