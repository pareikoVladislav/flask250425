from flask import Flask

from src.core.config import settings


def init_database(app: Flask) -> None:
    ...


def register_routers(app: Flask) -> None:
    from src.routers.questions import questions_bp

    app.register_blueprint(questions_bp)



def create_app(app: Flask) -> None:
    app.config.update(settings.get_flask_config())

    init_database(app)
    register_routers(app)
