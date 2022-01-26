class News:

    def __init__(self,name,author,title,description,urlToImage,publishedAt,content):

        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

class Source:

    def __init__(self,name,description,url,category,language,country):
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country