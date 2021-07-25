import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Yektanet.settings')

app = Celery('Yektanet')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



app.conf.beat_schedule = {
    "number_of_views_clicks_lastHour": {
        "task": "advertiser_mangement.tasks.summary_in_last_hour",
        "schedule": crontab(hour="*", minute=0)
    },
    "number_of_views_clicks_lastDay": {
        "task": "advertiser_mangement.tasks.summary_in_last_day",
        "schedule": crontab(hour=0, minute=0)
    }
}