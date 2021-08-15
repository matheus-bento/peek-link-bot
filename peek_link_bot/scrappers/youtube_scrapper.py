from peek_link_bot.scrappers.scrapper import Scrapper

class YoutubeScrapper(Scrapper):
    def __init__(self, dom):
        self.dom = dom
        self.get_data()
    
    def get_data(self):
        author_element = self.dom.find("span", attrs={ "itemprop": "author" })

        self.data = {
            "video_url": self.dom.find("link", attrs={ "itemprop": "url" }).attrs["href"],
            "title": self.dom.find("meta", attrs={ "itemprop": "name" }).attrs["content"],
            "channel_name": author_element.contents[1].attrs["content"]
        }

    def get_info(self):
        comment = ("# YouTube\n\n"
                   "## [{0}]({1}) - {2}\n\n"
                   "---\n"
                   "^(beep bop i'm /u/peek-link-bot, your friendly bot that checks links beforehand so you don't get bamboozled)")

        return comment.format(self.data["title"], self.data["video_url"], self.data["channel_name"])
