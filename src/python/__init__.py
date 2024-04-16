from flask import Flask

from database.db import get_db
from . import main, auth


def create_app() -> Flask:
    app = Flask(__name__)

    with app.app_context():
        get_db()

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)

    return app
