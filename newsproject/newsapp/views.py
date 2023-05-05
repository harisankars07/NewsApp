from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key='1fa32252fedf4101903bacc3a4123868')
    headLines = newsapi.get_top_headlines(sources = 'bbc-news , aftenposten')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    date=[]

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        date.append(article['publishedAt'])

    mylist = zip(news,desc,img,date)

    return render(request,"index.html",context= {"mylist":mylist})