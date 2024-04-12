import flask

app = flask.Flask(__name__)


@app.route("/")
def default():
    return flask.jsonify({"message": "Hello World"}), 200
