from celery import shared_task, task, chain, group
import requests
import datetime
requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup as bs

from teoapp.models import PostData

import time


#requests.packages.urlib3.disable_warnings()
from celery.schedules import timedelta, crontab

from teoapp.models import MyModel


@shared_task(queue='low_priority')
def taskdetector():
    t = datetime.datetime.now()
    s = str(t)
    models = MyModel.objects.all()
    for m in models:
        try:
            model = MyModel.objects.get(name = s)
        except MyModel.DoesNotExist:
            model = MyModel()
            model.name = s
            model.save()
            time.sleep(0.01)
    print(model)


@shared_task(max_retries=None, queue='high_priority')
def secondtask():
    listaWpisow = tworzenieModeli(ekstraktorStronWpisow(zbieraczStronBloga()))
    time.sleep(0.2)
    testBazdyDanych = PostData.objects.all().order_by('id').last()
    #engine = sqlalchemy.create_engine('sqlite:///./db.sqlite3')
    if testBazdyDanych:
        #print("znajduje się ostatni obiekt")
        print(testBazdyDanych.id)
        #with engine.connect() as con:
            #rs = con.execute(text("UPDATE sqlite_sequence SET seq=0 WHERE name='app_postdata'"))
        print("UPDATE")
    else:
        print("pusto")

        #with engine.connect() as con:
            #rs = con.execute(text("DELETE FROM sqlite_sequence WHERE name='app_postdata'"))
            #print("RESET")

    time.sleep(0.02)
    for wpis in listaWpisow:
        try:
            post = PostData.objects.get(_postTitle=str(wpis['title']))
            #print(f"istnieje model: {str(post)}")

        except PostData.DoesNotExist:

            # post = PostData(id=_id)

            post = PostData()
            post.postTitle = wpis['title']
            post.postURL = wpis['postUrl']
            post.postContent = wpis['content']
            post.postAuthor = wpis['author']
            post.postDate = wpis['postDate']
            post.save()
            time.sleep(0.01)
            #print(f"utworzono model {str(post)}")
    #return listaWpisow

def zbieraczStronBloga():
        teonitePages = []
        counter = 1
        while True:
            url = 'https://teonite.com/blog/page/'
            if counter == 1:
                url2 = 'https://teonite.com/blog/'
            else:
                url2 = url + str(counter) + '/'
            try:
                r = requests.get(url2)
                r.raise_for_status()
                _status_code = r.status_code
                if r.status_code is 200:
                    teonitePages.append(url2)
                    counter += 1
            except requests.exceptions.HTTPError as err:
                # print(err)
                break
        return teonitePages

def ekstraktorStronWpisow(teonitePages):
        postUrls = []
        for page in teonitePages:
            session = requests.Session()
            url = page
            content = session.get(url, verify=False).content
            soup = bs(content, "html.parser")
            articles = soup.find_all('h2', {'class': 'post-title'})

            for article in articles:
                _a = article.find('a').get('href')
                start = _a.find('blog')
                url = 'https://teonite.com/' + _a[start:]
                #print(url)
                postUrls.append(url)
        return postUrls

def tworzenieModeli(postUrls):
        models = []
        #model = {}
        for postUrl in postUrls:
            r = requests.get(postUrl).content
            s = bs(r, 'html.parser')
            date = s.find('span', {'class': 'blog-button post-date-button'}).get_text()
            postDate = datetime.datetime.strptime(date, '%d %b %Y')
            author = s.find('span', {'class': 'author-name'}).get_text()
            title = s.find('h1', {'class': 'post-title'}).get_text()
            content = s.find('div', {'class': 'post-content'}).get_text()

            model = {
                'postDate': postDate,
                'author': author,
                'title': title,
                'content': content,
                'postUrl': postUrl
            }
            models.append(model)

        return models