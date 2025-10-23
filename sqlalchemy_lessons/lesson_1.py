# "postgresql+psycopg2://my_user:strong_PASSWORD@localhost:5432/my_database"
# "mysql+pymysql://my_user:strong_PASSWORD@localhost:3306/my_database"
#
# "sqlite:///path/to/our/db/file.db"
# "sqlite:///:memory:"
# user = User(name="Igor")  # Transient
# session.add(user)  # Pending
# session.commit()  # Persistent
from typing import Optional

from sqlalchemy_lessons import String, Integer, create_engine, ForeignKey, Text, Table, Column
from sqlalchemy_lessons.orm import (
    sessionmaker,
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)
from pathlib import Path

BASE_DIR: Path = Path(__file__).parent.parent

# print(BASE_DIR)

DB_PATH: Path = BASE_DIR / 'test_database.db'

engine = create_engine(
    # url=f"sqlite:///{DB_PATH}",
    url=f"sqlite:///:memory:",
    echo=True  # !!!!!!!! ТОЛЬКО В РЕЖИМЕ ОТЛАДКИ !!!!!!!!
)


Session = sessionmaker(bind=engine)

session = Session()



class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )


users_projects = Table(
    'users_projects',
    Base.metadata,
    Column('user_id', ForeignKey('users.id')),
    Column('project_id', ForeignKey('projects.id')),
)



class User(Base):  # 'users'
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(String(30))
    surname: Mapped[Optional[str]] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(index=True, unique=True)
    rating: Mapped[float] = mapped_column(
        default=1.0,
    )
    age: Mapped[int]

    addresses: Mapped[list["Address"]] = relationship(
        'Address',
        back_populates='user'
    )
    projects: Mapped[list["Project"]] = relationship(
        secondary=users_projects,
        back_populates='users'
    )
    profile: Mapped["Profile"] = relationship(
        'Profile',
        back_populates='user',
        uselist=False
    )


class Project(Base):
    __tablename__ = 'projects'

    name: Mapped[str]
    description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True
    )

    users: Mapped[list["Project"]] = relationship(
        secondary=users_projects,
        back_populates='projects'
    )


class Address(Base):
    __tablename__ = 'addresses'

    country: Mapped[str] = mapped_column(String(20))
    city: Mapped[str] = mapped_column(String(60))
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('users.id')
    )

    user: Mapped["User"] = relationship(  # НЕ СОЗДАЁТСЯ НА УРОВНЕ БАЗЫ ДАННЫХ
        'User',
        back_populates='addresses'
    )


class Profile(Base):
    __tablename__ = 'profiles'

    experience: Mapped[int]
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('users.id'),
        unique=True
    )

    user: Mapped["User"] = relationship(
        'User',
        back_populates='profile',
        uselist=False
    )

Base.metadata.create_all(bind=engine)
