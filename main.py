import os, sys
import praw
from peek_link_bot.url import Url

def main():
    reddit = praw.Reddit(
        user_agent="Peek Link Bot",
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD")
    )

    for notification in reddit.inbox.stream():
        if notification.type == "username_mention" and not notification.is_root:
            parent = reddit.comment(notification.parent_id.split("_")[1])
            urls = Url.extract(parent.body)

            for mentioned_url in urls:
                url_info = Url(mentioned_url).get_info()
            
                notification.reply(url_info)
                notification.mark_read()

if __name__ == "__main__":
    main()
