from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Video(Base):
    __tablename__ = "videos"

    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str]
    channel_title: Mapped[str]
    description: Mapped[str]
    views_count: Mapped[int]
    likes_count: Mapped[int]
    comments_count: Mapped[int]
