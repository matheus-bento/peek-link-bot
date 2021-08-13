import re

import requests
from bs4 import BeautifulSoup

class Url:

    @staticmethod
    def extract(comment):
        url_re = re.compile(r'(?:https?:\/\/.)?(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b(?:[-a-zA-Z0-9@:%_\+.~#?&//=]*)')

        matches = url_re.findall(comment)
        return matches

    def get_data(url):
        html = requests.get(url).text
        dom = BeautifulSoup(html, 'html.parser')

        # TODO: add a switch to test if the given url is from a well-known
        #       website in order to use its specific scrapper class
        
