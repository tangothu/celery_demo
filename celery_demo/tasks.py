# tasks.py
import time
from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def showMessage(msg):
    print('This is the message content {} from celery!...'.format(msg))
    time.sleep(2.0)
    print('Message sent and displayed.')
