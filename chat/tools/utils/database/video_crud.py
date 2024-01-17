from sqlalchemy.orm.session import Session

from .database import create_all, drop_all, get_db
from .helpers import get_videos
from .models import Video
from .schemas import CreateVideoSchema


def add_video_to_database(video: CreateVideoSchema, session: Session):
    video: Video = Video(**video.model_dump())
    with session() as db:
        db.add(video)
        db.commit()
        db.refresh(video)
    return video


def get_all_videos():
    with get_db() as db:
        videos: list[Video] = db.query(Video).all()
    return videos


def seed_database(
    query: str = "Python programming videos for beginners", max_results: int = 50
):
    drop_all()
    create_all()
    videos: list[CreateVideoSchema] = get_videos(query=query, max_results=max_results)
    for video in videos:
        add_video_to_database(video=video, session=get_db)
