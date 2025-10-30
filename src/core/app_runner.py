from flask import Flask

from src.core.config import settings
from src.core.db import db


def init_database(app: Flask) -> None:
    db.init_app(app)


def register_routers(app: Flask) -> None:
    from src.routers.questions import questions_bp

    app.register_blueprint(questions_bp)



def create_app(app: Flask) -> None:
    app.config.update(settings.get_flask_config())

    init_database(app)
    register_routers(app)
