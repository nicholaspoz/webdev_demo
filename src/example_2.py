from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, world!"


# Take input from the client
@app.route("/say-hello/<name>")
def say_hello(name):
    return f"Hello, {name} {name}!"
