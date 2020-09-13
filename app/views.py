from flask import render_template
from app import app
from .request import get_news, get_news


# views
@app.route('/news/<int:id>') 
def news(id):
    '''
     View news page function that returns the news details page and its data
    '''
    news= get_news(id)
    title= f'{movie.title}'

    return render_template{'news.html',title=title,news=news}
def index():

    '''
    view root page function that returns the index page and its data
    '''
    # Getting popular news
    popular_news = get_news('popular')
    upcoming_news = get_news('upcoming')
    now_showing_news = get_news('now_playing')
    title='Home- Welcome to the best news Review Website'
    return render_template('index.html',title=title, popular=popular_news)
def news(news_id):

    '''
    view root page function that returns the index page and its data
    '''
    news_id='Home- List of News channels'
    return render_template('news.html', id= news_id)


