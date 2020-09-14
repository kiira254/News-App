from app import app
import urllib.request,json
from .models import news

News= news.News

# getting api key
api_key = None

#  getting the news base url
base_url= None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    function that gets the json response to our url request
    '''
    get_news_url= base_url.format( category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response=json.loads(get_news_data)

        news_results= None

        if get_news_response['results']:
            news_results_list= get_news_response['results']
            news_results = process_results(news_results_list)

    return news_results   

def process_results(news_list):
    '''
    function that processes the news result and transform them to a list of objects

        Args:
            news_list: A list of dictonaries that contain news details

        Returns:
            news_results: A list of news objects
    '''
    news_results=[]
    for news_item in news_list:
        id = news_item.get("id")
        name = news_item.get("name")
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        poster = news_item.get('poster_path')
        content = news_item.get ('content')
       
        if poster:
           news_object= News(id,name,author,title,description,poster,content)
           news_results.append(news_object)
        
    return news_object

def get_news(id):
    get_news_details_url=base_url.format(id,api_key)
    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data=url.read()
        news_details_response=json.load(news_details_data)

            news_object = None
            if news_details_response:
                id = news_details_response.get("id")
                name = news_details_response.get("name")
                author = news_details_response.get('author')
                title = news_details_response.get('title')
                description = news_details_response.get('description')
                poster = news_details_response.get('poster_path')
                content = news

                news_object= News(id,name,author,title,description,poster,content)

            return news_object
                


