from app import app
from flask import render_template
from .request import getNews


@app.route('/')
def home_page():
    top_headlines = getNews('everything')
    title = 'Welcome to Marcos News Channel'
    return render_template('index.html', title=title, headlines= top_headlines)
    