from celery import shared_task
from .models import Ad, Click, View, summaryShit
from datetime import datetime

@shared_task
def summary_in_last_hour():
    t = datetime.now()
    last_hour = t.replace(hour=int(t.strftime("%H"))-1)
    ad_list = Ad.objects.all()
    for ad in ad_list:
        NOview = View.objects.filter(viewID=ad, date__range=(last_hour, datetime.now())).count()
        new_obj = summaryShit(adID=ad, date=last_hour, count=NOview, view_or_click=1)
        new_obj.save()
        NOclick = Click.objects.filter(adID=ad, date__range=(last_hour, datetime.now())).count()
        new_obj = summaryShit(adID=ad, date=last_hour, count=NOclick, view_or_click=0)
        new_obj.save()


@shared_task
def summary_in_last_day():
    t = datetime.now()
    last_day = t.replace(day=int(t.strftime("%d"))-1)
    ad_list = Ad.objects.all()
    for ad in ad_list:
        NOview = summaryShit.objects.filter(adID=ad, date__range=(last_day, datetime.now()), view_or_click=1).count()
        new_obj = summaryShit(adID=ad, date=last_day, count=NOview, view_or_click=1)
        new_obj.save()
        NOclick = summaryShit.objects.filter(adID=ad, date__range=(last_day, datetime.now()), view_or_click=0).count()
        new_obj = summaryShit(adID=ad, date=last_day, count=NOclick, view_or_click=0)
        new_obj.save()



