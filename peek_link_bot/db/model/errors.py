from peek_link_bot.db.model.base import Base
from sqlalchemy import Column, Text, Integer
from datetime import datetime, timezone

class Errors(Base):
    __tablename__ = 'errors'

    comment_id = Column(Text, primary_key=True, nullable=False)
    message = Column(Text, nullable=False)
    error_utc = Column(Integer,
                       nullable=False,
                       default=int(datetime.now(timezone.utc).timestamp()))