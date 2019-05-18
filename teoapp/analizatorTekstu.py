import os
import nltk
import nltk.corpus
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import json
from collections import Counter
from teoapp.models import PostAuthor, PostContent
import time

additional_stop_words = ('one', 'like', 'us', 'also', 'new', 'use')
stop_words = set(stopwords.words('english'))
for sw in additional_stop_words:
    stop_words |= {sw}

def topTenAutora(autorName):
    try:
        autor = PostAuthor.objects.get(name=autorName)

        tokenizer = RegexpTokenizer(r'\w+')
        #stop_words = set(stopwords.words('english'))
        text = str(autor.posts)
        result = tokenizer.tokenize(text)
        ns = [token for token in result if token.lower() not in stop_words]
        fdist = nltk.FreqDist(ns)
        topTen = fdist.most_common(10)
        topTenDict = dict(topTen)
        return str(topTenDict)
    except PostAuthor.DoesNotExist:
        return ""


def topTenBlog(id):
    try:
        blog = PostContent.objects.get(id=id)
        tokenizer = RegexpTokenizer(r'\w+')
        #stop_words = set(stopwords.words('english'))
        text = str(blog.content)
        result = tokenizer.tokenize(text)
        ns = [token for token in result if token.lower() not in stop_words]
        fdist = nltk.FreqDist(ns)
        topTen = fdist.most_common(10)
        topTenDict = dict(topTen)
        return str(topTenDict)
    except PostContent.DoesNotExist:
        return ""

