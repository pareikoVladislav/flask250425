from flask import Blueprint
from typing import Any


questions_bp = Blueprint("questions", __name__, url_prefix='/questions')


# CRUD (Questions)

# R
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


# C
@questions_bp.route('/create', methods=["POST"])
def create_new_question() -> str:
    return "New Question was created"


# R
@questions_bp.route('/<int:question_id>', methods=["GET"])
def get_question_by_id(question_id: int) -> dict[str, Any]:
    return {
        "id": question_id,
        "title": "На сколько вы в шоке?"
    }


# U
@questions_bp.route('/<int:question_id>/update', methods=["PUT", "PATCH"])
def update_question(question_id: int) -> str:
    return f"Question with ID {question_id} was updated. Congrats!"


# D
@questions_bp.route('/<int:question_id>/delete', methods=["DELETE"])
def delete_question(question_id: int) -> str:
    return f"Question with ID {question_id} was deleted successfully. Congrats!"
