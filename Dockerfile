FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
# dodatnie poniże pojelecenia z instalacją paczki dla nltk ze stopwords, inaczej nie będzie tego widział program
RUN pip install -r requirements.txt && python -m nltk.downloader stopwords


