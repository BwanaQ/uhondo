import unittest
from models import source
Source = source.Source


class SourceTest(unittest.TestCase):
    def SetUp(self):
        '''
        SetUp method to initialize before any test
        '''
        self.new_source = Source("abc-news", "ABC News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",
                                 "https://abcnews.go.com", "general", "en", "us")

    def test_intsance(self):
        self.assertTrue(isinstance(self.new_source, Source))


if __name__ == '__main__':
    unittest.main()
