import example_4_db as db
from flask import Flask

app = Flask(__name__)


@app.route("/increment")
def increment():
    count = db.get_count()

    new_count = count + 1
    db.set_count(new_count)

    return {"count": new_count}


@app.route("/reset")
def reset():
    new_count = 0
    db.set_count(new_count)

    return {"count": new_count}


# When the server starts, initialize the db connection
with app.app_context():
    db.initialize()


# When the server stops, close the db connection
@app.teardown_appcontext
def close_connection(exception):
    db.close_connection(exception)
