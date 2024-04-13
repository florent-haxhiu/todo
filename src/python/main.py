from flask import jsonify, Blueprint


bp = Blueprint('rand', __name__, url_prefix='/api')


@bp.route("/")
def hello_world():
    return jsonify({"message": "Hello World"}), 200


@bp.route('/save')
def save_to_db():
    cur = get_db().cursor()
    print(cur.fetchall())
    return jsonify(cur.fetchall()), 200
