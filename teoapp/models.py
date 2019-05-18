from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=120)

class PostData(models.Model):
    _postTitle = models.CharField(max_length=120)
    postURL = models.TextField()
    postContent = models.TextField()
    postAuthor = models.CharField(max_length=120)
    postDate = models.CharField(max_length=120)

    def __str__(self):
        return f"Tytuł wpisu: {self.postTitle}, autor: {self.postAuthor}, url: {self.postURL}"

    @property
    def postTitle(self):
        return self._postTitle

    @postTitle.setter
    def postTitle(self, nowa):
        self._postTitle = nowa

class PostAuthor(models.Model):
    name = models.CharField(max_length=120)
    posts = models.TextField(blank=True)
    _topTen = models.TextField(blank=True)

    @property
    def topTen(self):
        return self._topTen

    @topTen.setter
    def topTen(self, value):
        self._topTen = value



class PostContent(models.Model):
    _content = models.TextField(blank=True)
    _topTen = models.TextField(blank=True)

    @property
    def topTen(self):
        return self._topTen

    @topTen.setter
    def topTen(self, value):
        self._topTen = value

    @property
    def content(self):
        return  self._content
    @content.setter
    def content(self, value):
        self._content = value

