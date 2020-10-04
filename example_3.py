import example_3_db as DB
from flask import Flask

app = Flask(__name__)


@app.route("/increment")
def increment():
    DB.increment()
    count = DB.get_count()
    return {"count": count}


@app.route("/reset")
def reset():
    DB.reset()
    count = DB.get_count()
    return {"count": count}


# When the server starts, initialize the DB connection
with app.app_context():
    DB.initialize()


# When the server stops, close the DB connection
@app.teardown_appcontext
def close_connection(exception):
    DB.close_connection(exception)
