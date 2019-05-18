import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teoproject.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('teoproject') # teoproject to nazwa projektu django, może być inna np. learning_log
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_heartbeat = None
app.conf.broker_connection_timeout = 30
app.autodiscover_tasks()

#backend='amqp'
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))