from app import app
import urllib.request
import json
from .models import article, source

Article = article.Article
Source = source.Source


# Getting api key
api_key = app.config['ARTICLE_API_KEY']
base_url = app.config['ARTICLE_API_BASE_URL']
source_url = app.config['ARTICLE_API_SOURCES_URL']


def get_sources():
    '''
    Function to get the json response to our url request
    '''

    get_sources_url = source_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_source_results(source_results_list)

    return source_results


def process_source_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        source_object = Source(
            id, name, description, url, category, language, country)
        source_results.append(source_object)
    return source_results


def get_articles(id):
    '''
    Function to get the json response to our url request
    '''

    get_articles_url = base_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_results(article_results_list)

    return article_results


def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        url_to_image = article_item.get('urlToImage')
        published_at = article_item.get('publishedAt')
        content = article_item.get('content')
        article_object = Article(
            author, title, description, url, url_to_image, published_at, content)
        article_results.append(article_object)
    return article_results
