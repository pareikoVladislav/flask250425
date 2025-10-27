from flask import Flask

from src.core.config import settings


def init_database(app: Flask) -> None:
    ...


def register_routers(app: Flask) -> None:
    ...


def create_app(app: Flask) -> None:
    app.config.update(settings.get_flask_config())

    init_database(app)
    register_routers(app)
