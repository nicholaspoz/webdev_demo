from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, world!"


# Take input from the client
@app.route("/say-hello/<name>")
def say_hello(name):
    return f"Hello, {name}!"


# Serve JSON
@app.route("/dogs")
def get_dogs():
    return {
        "results": [
            {"name": "Scooby", "age": 9, "owner": "Shaggy"},
            {"name": "Scrappy", "age": 2, "owner": "Nobody knows?"},
        ]
    }
