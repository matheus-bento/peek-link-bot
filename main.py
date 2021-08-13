import praw
from url import Url

reddit = praw.Reddit('peek-link-bot')

for item in reddit.inbox.stream():
    if item.type == 'username_mention' and not item.is_root:
        parent = reddit.comment(item.parent_id.split('_')[1])
        urls = Url.extract(parent.body)

        for mentioned_url in urls:
            Url.get_data(mentioned_url)
            pass

