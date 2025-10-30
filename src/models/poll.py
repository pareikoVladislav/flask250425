from datetime import datetime
from sqlalchemy import String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base


class Poll(Base):
    __tablename__ = 'polls'

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_anonymous: Mapped[bool] = mapped_column(Boolean, default=True)

    # Связи
    options: Mapped[list["PollOption"]] = relationship(
        back_populates="poll",
        cascade="all, delete-orphan"
    )
    votes: Mapped[list["Vote"]] = relationship(
        back_populates="poll",
        cascade="all, delete-orphan"
    )
    statistics: Mapped["PollStatistics"] = relationship(
        back_populates="poll",
        uselist=False,  # One-to-One отношение
        cascade="all, delete-orphan"
    )



class PollOption(Base):
    __tablename__ = 'poll_options'

    poll_id: Mapped[int] = mapped_column(ForeignKey('polls.id'), nullable=False)
    text: Mapped[str] = mapped_column(String(255), nullable=False)

    # Связи
    poll: Mapped["Poll"] = relationship(back_populates="options")
    votes: Mapped[list["Vote"]] = relationship(back_populates="option")
