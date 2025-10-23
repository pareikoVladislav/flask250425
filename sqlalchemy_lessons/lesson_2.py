# CRUD

import os
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy import create_engine
from pathlib import Path
from dotenv import load_dotenv

from sqlalchemy_lessons.social_blogs_models import User
from sqlalchemy_lessons.schemas import UserCreateSchema, UserResponseSchema

from sqlalchemy_lessons.db import DBConnector


BASE_DIR = Path(__file__).parent.parent

load_dotenv(BASE_DIR / ".env")

DB_URL= os.getenv("DB_URL")


engine = create_engine(
    url=DB_URL
)


def create_user(session, raw_data):
    try:
        validated_data = UserCreateSchema.model_validate_json(raw_data)

        user = User(**validated_data.model_dump())

        session.add(user)
        session.commit()

        return UserResponseSchema.model_validate(user)

    except ValidationError as exc:
        raise ValueError(f"Error: {exc}")

    except (IntegrityError, DataError) as exc:
        session.rollback()

        raise exc


def get_user_by_id(session, user_id):
    user = session.get(User, user_id)

    if not user:
        raise ValueError(
            f"User with ID {user_id} not found"
        )

    return UserResponseSchema.model_validate(user)


with DBConnector(engine) as session:
    # json_data = """{
    #     "first_name": "John",
    #     "last_name": "Green",
    #     "email": "john.green@gmail.com",
    #     "password": "MySecurePassword",
    #     "repeat_password": "MySecurePassword",
    #     "phone": "+1 234 567 8901",
    #     "role_id": 3
    # }"""
    #
    # try:
    #     created_user = create_user(session=session, raw_data=json_data)
    #
    #     print("OUR USER WAS CREATED")
    #     print(created_user)
    # except Exception as err:
    #     print(f"ERROR: {err}")

    try:
        user = get_user_by_id(session=session, user_id=5)

        print("USER WAS FOUND")
        print(user.model_dump_json(indent=4))
    except ValueError as exc:
        print(exc)
