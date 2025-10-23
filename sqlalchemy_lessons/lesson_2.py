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


with DBConnector(engine) as session:
    json_data = """{
        "first_name": "John",
        "last_name": "Green",
        "email": "john.green@gmail.com",
        "password": "MySecurePassword",
        "repeat_password": "MySecure123Password",
        "phone": "+1 234 567 8901",
        "role_id": 3
    }"""

    try:
        created_user = create_user(session=session, raw_data=json_data)

        print("OUR USER WAS CREATED")
    except Exception as err:
        print(f"ERROR: {err}")
