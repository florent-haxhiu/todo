from flask import jsonify, Blueprint

from database.db import get_db

bp = Blueprint('rand', __name__, url_prefix='/api')


@bp.route("/")
def hello_world():
    return jsonify({"message": "Hello World"}), 200


@bp.route('/save', methods=['GET', 'POST'])
def save_to_db():
    cur = get_db().cursor()
    # cur.execute("")
    print(cur.fetchall())
    return jsonify(cur.fetchall()), 200
