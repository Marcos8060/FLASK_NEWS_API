from app import app
from flask import render_template
from .request import getNews


@app.route('/')
def home_page():
    everything = getNews('everything')
    title = 'Welcome to Marcos News Channel'
    return render_template('index.html', title=title, everything= everything)

@app.route('/headlines')
def headlines_page():
    headlines = getNews('top-headlines')
    return render_template('headlines.html', headlines= headlines)

app.route('/sources')
def sources_page():
    sources = getNews('top-headlines,sources')
    return render_template('sources.html',sources=sources)
    