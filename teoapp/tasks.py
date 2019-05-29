from celery import shared_task, task, chain, group
import requests
import datetime
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup as bs
from teoapp.models import PostData
import time
from teoapp.models import PostAuthor, PostContent
from teoapp.analizatorTekstu import topTenAutora, topTenBlog
#from celery.schedules import crontab, timedelta
#from celery.task import periodic_task

#@periodic_task(run_every=(timedelta(seconds=180)), name='author_creator')
@shared_task(queue='low_priority', name='author_creator')
def author_creator():
    authors = PostData.objects.all()
    for a in authors:
        name = a.postAuthor
        try:
            postauthor = PostAuthor.objects.get(name = name)
            posts = PostData.objects.filter(postAuthor=postauthor.name)

            content = ""
            #topTen = ""
            for p in posts:
                content += (str(f"{p.postContent}") + "\n\n\n\n")
            postauthor.posts = content
            topTen = topTenAutora(postauthor.name)
            if postauthor.topTen == topTen and postauthor.topTen != "":
                postauthor.save()
            else:
                postauthor.topTen = topTen
                postauthor.save()
        except PostAuthor.DoesNotExist:
            postauthor = PostAuthor()
            postauthor.name = name
            postauthor.save()
            time.sleep(0.01)

#@periodic_task(run_every=(timedelta(seconds=220)), name='blogContent')
@shared_task(queue='blog', name='blogContent')
def blogContent():
    authors = PostAuthor.objects.all()
    content = ""
    for a in authors:
        c = str(a.posts)
        content += c
    try:
        blogContent = PostContent.objects.get(id=1)
        blogContent.content = content
        topTen = topTenBlog(blogContent.id)
        print(topTen)

        blogContent.topTen = topTen
        blogContent.save()
        time.sleep(0.01)

    except PostContent.DoesNotExist:
        blogContent= PostContent(id=1)
        blogContent.content = content
        blogContent.save()
        time.sleep(0.01)

#@periodic_task(run_every=(timedelta(seconds=120)), name='scraper')
@shared_task(queue='high_priority', name='scraper')
def scraper():
    listaWpisow = tworzenieModeli(ekstraktorStronWpisow(zbieraczStronBloga()))
    time.sleep(0.05)
    for wpis in listaWpisow:
        try:
            post = PostData.objects.get(_postTitle=str(wpis['title']))
            if post.postDate != str(wpis['postDate']):
                print(f"{post.postDate} != {str(wpis['postDate'])}")
                post.postDate = wpis['postDate']
                post.postContent = wpis['content']
                post.save()
                time.sleep(0.01)

            else:
                continue

        except PostData.DoesNotExist:
            post = PostData()
            post.postTitle = wpis['title']
            post.postURL = wpis['postUrl']
            post.postContent = wpis['content']
            post.postAuthor = wpis['author']
            post.postDate = wpis['postDate']
            post.save()
            time.sleep(0.01)

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
                #print(url2)
                r = requests.get(url2)
                r.raise_for_status()
                _status_code = r.status_code
                if r.status_code is 200:
                    teonitePages.append(url2)
                    counter += 1
            except requests.exceptions.HTTPError as err:
                break
        #print(f"Stron na blogu: {len(teonitePages)}")
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