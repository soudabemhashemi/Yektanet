from django import template
from django.db.models.aggregates import Avg
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Ad, Advertiser, Click, View
from django.template import loader
from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import redirect
from django.template.response import TemplateResponse
import datetime
from django.db.models import Count, F
import itertools
from datetime import datetime

def countViews(request, post_ids):
    for post_id in post_ids:
        ad = Ad.objects.get(id = post_id.id)
        ip = request.ip
        newView = View(viewID=ad, date=datetime.now(), ip=ip)
        newView.save()

class HomePageView(TemplateView):
    template_name = "home.html"
    View.objects.filter(id=73).delete()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad_list'] = Ad.objects.all()
        context['advertiser_list'] = Advertiser.objects.all()
        countViews(self.request, context['ad_list'])
        return context

class countClicks(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        ad = Ad.objects.get(pk=kwargs['pk'])
        newClick = Click(adID=ad, date=datetime.now(), ip='127.0.0.1')
        newClick.save()
        return ad.link

def createAd(request):
    if request.method == "POST":
        title = request.POST['title']
        imgUrl = request.POST['image']
        link = request.POST['url']
        advertiser = Advertiser.objects.get(id=request.POST['advertiser'])
        ins = Ad(title=title, imgUrl=imgUrl, link=link, advertiser=advertiser)
        ins.save()
        return redirect('advertiser_mangement:home')
    return render(request, 'create_new.html')


def report(request):
    pass
    # q1 = Click.objects.values('adID', 'date')
    # q2 = View.objects.values('adID', 'date')
    # q3 = Click.objects.values('adID', 'date').union(View.objects.values('adID', 'date')).order_by('adID')
    # print(Click.objects.values('adID', 'date').union(View.objects.values('adID', 'date')).order_by('adID').datetimes('date', 'hour').count())
    # print(Click.objects.exclude(adID__title = 'title2')) 
    # print(Click.objects.filter(adID__title = 'title1').datetimes('date', 'hour').count())
    # print(Click.objects.filter(date = datetime.datetime(2021, 7, 14, 8, 0)).filter(adID__title = 'title1').count())
    # print(Click.objects.datetimes('date', 'hour'))
    # print(View.objects.datetimes('date', 'hour').count())
    # print(View.objects.filter(clicks__adID_id=))
    ad_list = Ad.objects.all()
    # date_list = Click.objects.datetimes('date','hour').order_by('date')
    # print(ad_list, date_list)
    # for ad in ad_list:
    #     print(Click.objects.filter(adID=ad)
    #             .extra({'date_created': "time(date)"})
    #             .values('date_created')
    #             .annotate(created_count=Count('date'))
    #     )
    #     print(View.objects.filter(adID=ad)
    #             .extra({'date_created': "time(date)"})
    #             .values('date_created')
    #             .annotate(created_count=Count('id'))
    #     )
    #     print("________________________________________")

    def date_hour(timestamp):
        return timestamp.strftime("%H")

    date_list = Click.objects.values('date')
    view_list_date = View.objects.values('date')

    for a in ad_list:
        objs = Click.objects.filter(
            date__range=(date_list[0]['date'],date_list.last()['date']),
            adID=a,
        )
        objs.union(View.objects.filter(
            date__range=(view_list_date[0]['date'], view_list_date.last()['date']),
            viewID=a
        ))
        groups = itertools.groupby(objs, lambda x: date_hour(x.date))
        for group, matches in groups:
            print(group, "TTL:", sum(1 for _ in matches))
        print("_______________________________")

    # print(groups)
    # print(objs)
    # since groups is an iterator and not a list you have not yet traversed the list
    
    # print(Click.objects.all().aggregate(avg_diff=Avg(F('date')-F('date'))))
    # q1 = Click.objects.select_related('adID')
    # q2 = View.objects.select_related('adID')
    # print(q1.values('ip','adID__id','date').intersection(q2.values('ip', 'adID__id', 'date')))

    # clicks = Click.objects.all()

    # def date_hour(a,b):
    #     e = a.strftime("%H")
    #     ee = b.strftime("%H")
    #     print(ee-e)

    # for c in clicks:
    #     view = View.objects.filter(
    #         adID = c.adID,
    #         ip = c.ip
    #     )

    #     date_hour(c.date, view[0].date)
        # s = 0
        # for v in view:
        #     s += abs(c.date - v.date)
        
        # print(s)

    