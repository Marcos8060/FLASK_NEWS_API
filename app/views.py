from app import app
from flask import render_template
from .request import getNews
# import requests,json


@app.route('/')
def home_page():
    everything = getNews('everything')
    title = 'Welcome to Marcos News Channel'
    return render_template('index.html', title=title, everything= everything)

@app.route('/headlines')
def headlines_page():
    headlines = getNews('top-headlines')
    return render_template('headlines.html', headlines= headlines)

# app.route('/sources')
# def sources_page():
#      SOURCES_URL = 'https://newsapi.org/v2/top-headlines/sources?q=Apple&from=2022-01-25&sortBy=popularity&apiKey=d44a6ca7a2ff42faadd9361e56530005'
#      data = requests.get(SOURCES_URL).json()['sources']
#      return render_template('sources.html',sources = data)
    