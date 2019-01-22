from celery_task.tasks import celery_add

if __name__ == '__main__':
    celery_add.delay(2, 10)
