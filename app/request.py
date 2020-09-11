from app import app
from urllib.request,json
from .models import news

News= news.News

# getting api key
api_key = app.config['NEWS_API_KEY']

#  getting the news base url
base_url= app.config['NEWS_API_BASE_URL']