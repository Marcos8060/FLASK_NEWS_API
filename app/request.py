from app import app
import urllib.request,json
from .models import news

News = news.News

# get api key
api_key = app.config['API_KEY']
# base url
base_url = app.config['BASE_URL']


def getNews(category):

    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    # name,author,title,description,urlToImage,publishedAt,content
    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')
        url = news_item.get('url')

        if urlToImage:
            news_object = News(name,author,title,description,urlToImage,publishedAt,content,url)
            news_results.append(news_object)

    return news_results



