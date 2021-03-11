from flask import Flask

app = Flask(__name__)

# When the server starts, set the count to zero
count = 0


@app.route("/increment")
def increment():
    global count
    count += 1
    return f"You incremented to {count} !"


@app.route("/reset")
def reset():
    global count
    count = 0
    return {"count": count}
