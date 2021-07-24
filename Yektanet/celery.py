import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Yektanet.settings')

app = Celery('Yektanet')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task
def test():
    print("arg")


app.conf.beat_schedule = {
    "test-test": {
        "task": "test",
        "schedule": 60
    }
}