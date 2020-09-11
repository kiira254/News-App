from flask import render_template
from app import app

# views
@app.route('/news/<int:news_id>') 

def index()

    '''
    view root page function that returns the index page and its data
    '''
    title='Home- Welcome to the best news Review Website'
    return render_template('index.html',title=title)
def news(news_id):

    '''
    view root page function that returns the index page and its data
    '''
    news_id='Home- List of News channels'
    return render_template('news.html', id= news_id)


