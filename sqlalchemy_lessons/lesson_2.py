# CRUD

import os
from typing import Annotated, Optional

from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy import create_engine
from pathlib import Path
from dotenv import load_dotenv

from sqlalchemy_lessons.social_blogs_models import User, News, Role, Comment
from sqlalchemy_lessons.schemas import UserCreateSchema, UserResponseSchema

from sqlalchemy_lessons.db import DBConnector

#
# BASE_DIR = Path(__file__).parent.parent
#
# load_dotenv(BASE_DIR / ".env")
#
# DB_URL= os.getenv("DB_URL")
#
#
# engine = create_engine(
#     url=DB_URL
# )
#
#
# def create_user(session, raw_data):
#     try:
#         validated_data = UserCreateSchema.model_validate_json(raw_data)
#
#         user = User(**validated_data.model_dump())
#
#         session.add(user)
#         session.commit()
#
#         return UserResponseSchema.model_validate(user)
#
#     except ValidationError as exc:
#         raise ValueError(f"Error: {exc}")
#
#     except (IntegrityError, DataError) as exc:
#         session.rollback()
#
#         raise exc
#
#
# def get_user_by_id(session, user_id):
#     user = session.get(User, user_id)
#
#     if not user:
#         raise ValueError(
#             f"User with ID {user_id} not found"
#         )
#
#     return UserResponseSchema.model_validate(user)


from sqlalchemy import select, and_, or_, not_, desc, func

# with DBConnector(engine) as session:
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

    # try:
    #     user = get_user_by_id(session=session, user_id=5)
    #
    #     print("USER WAS FOUND")
    #     print(user.model_dump_json(indent=4))
    # except ValueError as exc:
    #     print(exc)

    # stmt = select(User)  # SELECT * FROM 'users'
    # stmt = select(User).where(User.role_id == 3)
    # stmt = select(
    #     User.email,
    #     User.role_id
    # ).where(User.role_id == 3)
    #
    # print("RAW QUERY")
    # print(stmt)
    # print("RAW QUERY")
    # users = session.execute(stmt).scalars().all()
    #
    # print(users)

    # for u in users:  # type: User
    #     print(u.email)


    # stmt = select(User).where(User.rating > 5)
    #
    # data = session.execute(stmt).scalars().all()
    #
    # print(data)
    #
    # resp = [
    #     UserResponseSchema.model_validate(u)
    #     for u in data
    # ]
    #
    # print(resp)

    # stmt = select(User).where(User.last_name.like("B%"))
    #
    # print(stmt)
    #
    # data = session.execute(stmt).scalars().all()
    #
    # print(data)
    #
    # resp = [
    #     UserResponseSchema.model_validate(u)
    #     for u in data
    # ]
    #
    # print(resp)

    # stmt = select(User).where(User.rating.between(5, 7))
    #
    # print(stmt)
    #
    # data = session.execute(stmt).scalars().all()
    #
    # print(data)
    #
    # resp = [
    #     UserResponseSchema.model_validate(u)
    #     for u in data
    # ]
    #
    # print(resp)


    # stmt = (
    #     select(User.email, User.role_id, User.rating)
    #     .where(
    #         and_(
    #             User.role_id == 3,
    #             User.rating < 6
    #         )
    #     ).order_by(User.rating)
    # )
    #
    # print(stmt)
    #
    # data = session.execute(stmt).scalars().all()
    #
    # print(data)
    #
    # for u in data:  # type: User
    #     # print(u.email, u.rating, u.role_id)
    #     print(u)


    # stmt = (
    #     select(
    #         User.role_id,
    #         func.avg(User.rating)
    #     ).group_by(User.role_id)
    # )
    #
    # print(stmt)
    #
    # data = session.execute(stmt).all()
    #
    # print(data)

    # stmt = (
    #     select(
    #         User.role_id,
    #         func.count(User.id)
    #     ).group_by(User.role_id)
    # )
    #
    # print(stmt)
    #
    # data = session.execute(stmt).all()
    #
    # print(data)

    # stmt = (
    #     select(
    #         func.count(News.id)
    #     ).where(
    #         News.moderated == 1
    #     )
    # )
    #
    # print(stmt)
    #
    # data = session.execute(stmt).scalar()
    #
    # print(data)

from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker


BASE_DIR = Path(__file__).parent.parent

load_dotenv(BASE_DIR / ".env")

DB_URL= os.getenv("DB_URL")


engine = create_engine(url=DB_URL)
session = sessionmaker(bind=engine)()

stmt = (
    select(User.id, User.first_name, User.rating)
    .where(and_(User.rating > 5, User.role_id==3))
)

print(stmt)


data = session.execute(stmt).all()


for user in data:
    print(user)


session.close()
