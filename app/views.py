from flask import render_template
from app import app
from .request import get_news

# views
@app.route('/') 

def index():

    '''
    view root page function that returns the index page and its data
    '''
    # Getting popular news
    popular_news = get_news('popular')
    print(popular_news)
    title='Home- Welcome to the best news Review Website'
    return render_template('index.html',title=title popular=popular_news)
def news(news_id):

    '''
    view root page function that returns the index page and its data
    '''
    news_id='Home- List of News channels'
    return render_template('news.html', id= news_id)


