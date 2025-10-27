from flask import Blueprint
from typing import Any


questions_bp = Blueprint("questions", __name__, url_prefix='/questions')


@questions_bp.route('', methods=["GET"])
def list_of_questions() -> list[dict[str, Any]]:
    return [
        {
            "id": 1,
            "title": "На сколько вы в шоке?"
        },
        {
            "id": 2,
            "title": "Вы точно в порядке?"
        }
    ]
