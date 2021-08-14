class YoutubeScrapper:
    def __init__(self, dom):
        self.dom = dom

    def get_data(self):
        author_element = self.dom.find('span', attrs={ 'itemprop': 'author' })

        return {
            'title': self.dom.find('meta', attrs={ 'itemprop': 'name' }).attrs['content'],
            'channel_name': author_element.contents[1].attrs['content'],
            'channel_url': author_element.contents[0].attrs['href']
        }