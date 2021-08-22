import re
import requests
from bs4 import BeautifulSoup

from peek_link_bot.scrappers.youtube_scrapper import YoutubeScrapper

# regex to match any valid URL
URL_RE = re.compile(r'(?:https?:\/\/.)?(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b(?:[-a-zA-Z0-9@:%_\+.~#?&//=]*)')

YOUTUBE_URL_RE = re.compile(r'(?:http|https)://(?:(?:(?:www\.)?youtube.com)|youtu.be)(?:[/\w]*(?:\?(?:[\w\-_]+=[\w\-_]+)*)?)')

class Url:
    def __init__(self, url):
        html = requests.get(url).text
        dom = BeautifulSoup(html, 'html.parser')
        
        if (YOUTUBE_URL_RE.match(url) != None):
            self.scrapper = YoutubeScrapper(dom)
        else:
            raise Exception("There are no scrappers to extract data from " + url)

    @staticmethod
    def extract(comment):
        # reddit returns an escaped comment string
        # we need to remove those backslashes in order
        # to get the actual URLs
        comment = comment.replace('\\', '')
        return URL_RE.findall(comment)

    def get_info(self):
        return self.scrapper.get_info()
