from flask import Flask

from . import auth
from . import main


def create_app() -> Flask:
    app = Flask(__name__)

    with app.app_context():
        pass

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)

    return app
