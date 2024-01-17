import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, sessionmaker


class Base(MappedAsDataclass, DeclarativeBase):
    pass


SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def create_all():
    Base.metadata.create_all(bind=engine)


def drop_all():
    Base.metadata.drop_all(bind=engine)


@contextmanager
def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()
