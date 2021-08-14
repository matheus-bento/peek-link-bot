import praw
from peek_link_bot.url import Url

def main():
    reddit = praw.Reddit('peek-link-bot',)

    for item in reddit.inbox.stream():
        if item.type == 'username_mention' and not item.is_root:
            parent = reddit.comment(item.parent_id.split('_')[1])
            urls = Url.extract(parent.body)

            for mentioned_url in urls:
                print(Url(mentioned_url).get_data())
                pass

if __name__ == "__main__":
    main()
