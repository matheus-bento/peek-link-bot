import praw

from peek_link_bot.url import Url
from peek_link_bot.db.database import Database

def main():
    reddit = praw.Reddit("peek-link-bot",)

    db = Database("sqlite:///peek_link_bot/db/comments.sqlite")
    db.generate()

    for item in reddit.inbox.stream():
        if item.type == "username_mention" and not item.is_root:
            parent = reddit.comment(item.parent_id.split("_")[1])
            urls = Url.extract(parent.body)

            for mentioned_url in urls:
                print(Url(mentioned_url).get_info())

if __name__ == "__main__":
    main()
