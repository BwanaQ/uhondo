import unittest
from models import article
Article = article.Article


class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of Article class
    '''

    def setUp(self):
        '''
        Method that runs before every test
        '''
        self.new_article = Article(
            "Tom Hunja", "Test Article", "Lorem Ipsum", "#", "#", "2021-02-20", "Lorem Ipsum")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))


if __name__ == '__main__':
    unittest.main()
