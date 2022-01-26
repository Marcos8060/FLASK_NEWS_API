from app import app
import urllib.request,json
from .models import news

News = news.News
Source = news.Source

# get api key
api_key = app.config['API_KEY']
# base url
base_url = app.config['BASE_URL']
# sources url
source_url = app.config['SOURCES_URL']

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

        if urlToImage:
            news_object = News(name,author,title,description,urlToImage,publishedAt,content)
            news_results.append(news_object)

    return news_results

# getting news source
def getnews_Source(category):

    getsource_url = source_url.format(category,api_key)

    with urllib.request.urlopen(getsource_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_sources(source_results_list)

    return source_results

def process_sources(source_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    # name,description,url,category,language,country
    source_results = []
    for source_item in source_list:
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if language == 'en':
            source_object = Source(name,author,description,url,category,language,country)
            source_results.append(source_object)

    return source_results


