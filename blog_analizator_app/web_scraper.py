import requests
import datetime
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup as bs


class modelScraper:
    @staticmethod
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
                # print(url2)
                r = requests.get(url2)
                r.raise_for_status()
                _status_code = r.status_code
                if r.status_code is 200:
                    teonitePages.append(url2)
                    counter += 1
            except requests.exceptions.HTTPError as err:
                break
        print(f"Stron na blogu: {len(teonitePages)}")
        return teonitePages

    @staticmethod
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
        print(f"Linków na blogu: {len(postUrls)}")
        return postUrls

    @staticmethod
    def tworzenieModeli(postUrls):
        models = []
        # model = {}
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