import os
import praw

from peek_link_bot.log import LoggingLevel, log
from peek_link_bot.comment_handler import CommentHandler

greeting = "^(beep bop i'm /u/peek-link-bot, your friendly bot that checks links beforehand so you don't get bamboozled)"

def main():
    reddit = praw.Reddit(
        user_agent="Peek Link Bot",
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD")
    )

    for notification in reddit.inbox.unread():
        if notification.type == "username_mention" and not notification.is_root:
            parent = reddit.comment(notification.parent_id.split("_")[1])

            try:
                handler = CommentHandler(parent.body)
                links_info = handler.get_links_info()

                message = '\n'.join(links_info) + '\n' + greeting
                notification.reply(message)

                log("Comment ID: " + notification.id + " " +
                    "Permalink: https://reddit.com" + notification.context + " " +
                    "Comment answered successfully", LoggingLevel.INFO)
            except Exception as e:
                log("Comment ID: " + notification.id + " " +
                    "Permalink: https://reddit.com" + notification.context + " " +
                    "Error: '" + str(e) + "'", LoggingLevel.ERROR)
            finally:
                notification.mark_read()

if __name__ == "__main__":
    main()
