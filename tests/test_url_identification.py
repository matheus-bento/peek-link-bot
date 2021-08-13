import unittest
import peek_link_bot.url as url

class TestURLIdentification(unittest.TestCase):
    def test_youtube_full_url(self):
        self.assertTrue(url.YOUTUBE_URL_RE.match('https://www.youtube.com/watch?v=dQw4w9WgXcQ') != None)

    def test_youtube_short_url(self):
        self.assertTrue(url.YOUTUBE_URL_RE.match('https://youtu.be/dQw4w9WgXcQ') != None)
    
    def test_invalid_youtube_full_url(self):
        self.assertTrue(url.YOUTUBE_URL_RE.match('https://ww.youtube.com/watch?v=dQw4w9WgXcQ') == None)
    
    def test_invalid_youtube_short_url(self):
        self.assertTrue(url.YOUTUBE_URL_RE.match('https://yout.ube/dQw4w9WgXcQ') == None)

    def test_greater_than_2(self):
        self.assertTrue(1 > 2)
