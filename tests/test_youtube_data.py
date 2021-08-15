import unittest
from peek_link_bot.url import Url

class TestYouTubeData(unittest.TestCase):
    def setUp(self):
        self.url = Url("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def test_generated_comment_from_youtube(self):
        expected = ("# YouTube\n\n"
                   "## [Rick Astley - Never Gonna Give You Up (Official Music Video)](https://www.youtube.com/watch?v=dQw4w9WgXcQ) - Rick Astley\n\n"
                   "---\n"
                   "^(beep bop i'm /u/peek-link-bot, your friendly bot that checks links beforehand so you don't get bamboozled)")
        self.assertTrue(self.url.get_info(), expected)
