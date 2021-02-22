from flask import render_template
from app import app
from .request import get_articles, get_sources
# Views


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # getting us news
    #us_articles = get_articles('us')
    # print(us_articles)
    all_sources = get_sources()
    title = 'Uhondo | Home of the latest News'
    return render_template('index.html', title=title, sources=all_sources)


@app.route('/source/<string:id>')
def source(id):
    '''
    View aticles from one source function
    '''
    source = get_articles(id)
    #title = f'{article.name}'

    return render_template('source.html',  source=source)
