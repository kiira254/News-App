from flask import render_template
from app import app

# views
@app.route('/newspaper/<int:newspaper_id>') 
def newspaper(newspaper_id):

    '''
    view root page function that returns the index page and its data
    '''
    return render_template('newspaper.html', id= movie_id)