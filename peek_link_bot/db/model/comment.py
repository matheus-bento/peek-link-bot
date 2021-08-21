from peek_link_bot.db.model.base import Base
from sqlalchemy import Column, Text, Integer

class Comment(Base):
    __tablename__ = 'comments'

    comment_id = Column(Text, primary_key=True, nullable=False)
    created_utc = Column(Integer, nullable=False)
    replied_utc = Column(Integer)