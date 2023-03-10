from flask import Flask, jsonify, request

app = Flask(__name__)

people = [
    {"name": "John McAdams",
     "age": 45,
     "favourite_food": "Scrambled Eggs"}
]


@app.route("/api")
def get_people():
    return jsonify(people)


if __name__ == "__main__":
    app.run(debug=True)
