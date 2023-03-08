from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, world!</h1>"


@app.route("/user/<name>")
def print_name(name):
    return f"<h1>Hello, {name} </h1>"


@app.route("/dance")
def do_dance():
    return "<h1>Bad request</h1>", 400


if __name__ == "__main__":
    app.run(debug=True)
