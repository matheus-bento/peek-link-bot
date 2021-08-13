import re

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

    @staticmethod
    def extract(comment):
        matches = URL_RE.findall(comment)
        return matches

    def get_data(self):
        return self.scrapper.get_data()

        # TODO: add a switch to test if the given url is from a well-known
        #       website in order to use its specific scrapper class
        
