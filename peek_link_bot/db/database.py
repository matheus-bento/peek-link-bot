from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from peek_link_bot.db.model.base import Base
from peek_link_bot.db.model.comment import Comment
from peek_link_bot.db.model.error import Error

class Database:
    def __init__(self, path):
        self.__engine = create_engine(path)
        self.__sessionmaker = sessionmaker(bind=self.__engine)

    def generate(self):
        """Generates the database and creates the mapped tables"""
        Base.metadata.create_all(self.__engine)

    def get_session(self):
        return self.__sessionmaker()
