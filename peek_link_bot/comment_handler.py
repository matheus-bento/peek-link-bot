import re
import requests
from bs4 import BeautifulSoup

from peek_link_bot.scrappers.youtube_scrapper import YoutubeScrapper

# regex to match any valid URL
URL_RE = re.compile(r'(?:https?:\/\/.)?(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b(?:[-a-zA-Z0-9@:%_\+.~#?&//=]*)')

YOUTUBE_URL_RE = re.compile(r'(?:http|https)://(?:(?:(?:www\.)?youtube.com)|youtu.be)(?:[/\w]*(?:\?(?:[\w\-_]+=[\w\-_]+)*)?)')

class CommentHandler:
    """
    Initialize a URL instance that allows to extract information from a link
    """
    def __init__(self, comment):
        comment = comment.replace('\\', '')
        self.links = URL_RE.findall(comment)

    def get_links_info(self):
        links_info = list()

        for link in self.links:
            scrapper = None

            html = requests.get(link).text
            dom = BeautifulSoup(html, 'html.parser')

            if (YOUTUBE_URL_RE.match(link) != None):
                scrapper = YoutubeScrapper(dom)

            if (scrapper is not None):
                links_info.append(scrapper.get_info())

        return links_info
