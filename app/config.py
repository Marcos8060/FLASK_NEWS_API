from distutils.debug import DEBUG


class Config:
     
     BASE_URL = 'https://newsapi.org/v2/{}?q=Apple&from=2022-01-25&sortBy=popularity&apiKey=d44a6ca7a2ff42faadd9361e56530005'
     API_KEY = 'd44a6ca7a2ff42faadd9361e56530005'

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True