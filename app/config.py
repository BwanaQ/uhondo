class Config:
    '''
    General configuration parent class
    '''
    ARTICLE_API_SOURCES_URL = 'http://newsapi.org/v2/sources?apiKey={}'
    ARTICLE_API_BASE_URL = 'http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
