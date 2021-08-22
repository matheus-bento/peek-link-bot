import praw
from datetime import datetime, timezone

from peek_link_bot.url import Url
from peek_link_bot.db.database import Database

from peek_link_bot.db.model.comment import Comment
from peek_link_bot.db.model.error import Error

def main():
    reddit = praw.Reddit("peek-link-bot",)

    db = Database("sqlite:///peek_link_bot/db/comments.sqlite")
    db.generate()

    for item in reddit.inbox.stream():
        if item.type == "username_mention" and not item.is_root:
            parent = reddit.comment(item.parent_id.split("_")[1])
            urls = Url.extract(parent.body)

            with db.get_session() as session:
                for mentioned_url in urls:
                    comment_replied = session.query(Comment).filter(Comment.comment_id==item.id).first() is not None
                    comment_error = session.query(Error).filter(Error.comment_id==item.id).first() is not None

                    if not comment_replied and not comment_error:
                        try:
                            url_info = Url(mentioned_url).get_info()
                            item.reply(url_info)

                            comment = Comment(comment_id=item.id,
                                              created_utc=int(item.created_utc),
                                              replied_utc=int(datetime.now(timezone.utc).timestamp()))

                            session.add(comment)
                        except Exception as exception:
                            error = Error(comment_id=item.id,
                                          message=str(exception),
                                          error_utc=int(datetime.now(timezone.utc).timestamp()))

                            session.add(error)
                session.commit()


if __name__ == "__main__":
    main()
