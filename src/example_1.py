from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, world!"


@app.route("/say-hello/<input>")
def say_hello(input):
    return {"hello": input}
