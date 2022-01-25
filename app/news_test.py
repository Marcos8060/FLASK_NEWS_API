import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):

    def setUp(self):

        self.new_news = News('wired','Morgan Meaker','Global warming',
        'The world is suffering from global warming',
        'https://media.wired.com/photos/61ef508fe365ac4c3753094c/191:100/w_1280,c_limit/Business_EU%20Building-180405277.jpg',
        '22,07,2021','Like millions of other internet users in Europe, when Alexandra Geese')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()
