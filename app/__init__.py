import os

from flask import Flask
from flask.cli import load_dotenv
from flask_cors import CORS
from flask_migrate import Migrate


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    CORS(app)

    load_dotenv('.env')

    from app.config import config
    app.config.from_object(config)

    for key in ['TMP_FILE_PATH', 'PERMANENT_FILE_PATH']:
        os.makedirs(app.config[key], exist_ok=True)

    app.app_context().push()

    from app.db import db
    Migrate(app, db)
    db.init_app(app)

    from .models import (
        Currency, Order
    )

    from .routes import register_routes
    register_routes(app)

    return app


if __name__ == '__main__':
    create_app().run()
