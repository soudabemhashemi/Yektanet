from django.views.generic import ListView
from .models import Ad, Advertiser, Click, View
from advertiser_mangement import models

class AdListView(ListView):
    model = Advertiser
    template_name = 'home.html'




























# from django import template
# from django.db.models.aggregates import Avg
# from django.http import HttpResponse, HttpResponseRedirect, request
# from django.shortcuts import render, get_object_or_404
# from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView
# from rest_framework import serializers
# from .models import Ad, Advertiser, Click, View
# from django.template import loader
# from django.views.generic.base import TemplateView, RedirectView
# from django.shortcuts import redirect
# from django.template.response import TemplateResponse
# import datetime
# from django.db.models import Count, F
# import itertools
# from datetime import datetime, timedelta
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import AdvertiserSerializer, AdSerializer


# @api_view(['GET'])
# def homePage(request):
#     ads = Ad.objects.all()
#     serializer = AdSerializer(ads, many=True)
#     return Response(serializer.data)


# def countViews(request, post_ids):
#     for post_id in post_ids:
#         ad = Ad.objects.get(id = post_id.id)
#         ip = request.ip
#         newView = View(viewID=ad, date=datetime.now(), ip=ip)
#         newView.save()

# class HomePageView(TemplateView):
#     template_name = "home.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['ad_list'] = Ad.objects.all()
#         context['advertiser_list'] = Advertiser.objects.all()
#         countViews(self.request, context['ad_list'])
#         return context

# class countClicks(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         ad = Ad.objects.get(pk=kwargs['pk'])
#         newClick = Click(adID=ad, date=datetime.now(), ip='127.0.0.1')
#         newClick.save()
#         return ad.link

# def createAd(request):
#     if request.method == "POST":
#         title = request.POST['title']
#         imgUrl = request.POST['image']
#         link = request.POST['url']
#         advertiser = Advertiser.objects.get(id=request.POST['advertiser'])
#         ins = Ad(title=title, imgUrl=imgUrl, link=link, advertiser=advertiser)
#         ins.save()
#         return redirect('advertiser_mangement:home')
#     return render(request, 'create_new.html')


# def report(request):

#     def date_hour(timestamp):
#         return timestamp.strftime("%H")
#     date_list = Click.objects.values('date')
#     view_list_date = View.objects.values('date')
#     ad_list = Ad.objects.all()
#     for a in ad_list:
#         print("For Ad ", a.id)
#         objs = Click.objects.filter(
#             date__range=(date_list[0]['date'],date_list.last()['date']),
#             adID=a,
#         )
#         groups = itertools.groupby(objs, lambda x: date_hour(x.date))
#         for group, matches in groups:
#             print("Clock: ", group, "TTL:", sum(1 for _ in matches))
#         print("_______________________________")

#     ###########
#     view_list_date = View.objects.values('date').order_by('date')
#     for v in view_list_date:
#         Noclicks = Ad.objects.all().filter(myClicks__date=v['date']).count()
#         NOview = Ad.objects.all().filter(myViews__date=v['date']).count()
#         print(Noclicks/NOview)
    
#     ############
#     sum1 = 0
#     selectedView = None
#     for ad in Ad.objects.values('id'):
#         for click in Ad.objects.get(id=ad['id']).myClicks.all():
#             for view in Ad.objects.get(id=ad['id']).myViews.all():
#                 if click.ip == view.ip and view.date < click.date:
#                     selectedView = view
#                     time2 = click.date - selectedView.date
#                     sum1 += time2.seconds
#             if Ad.objects.get(id=ad['id']).myClicks.count() != 0:
#                 avg = round(sum1 / Ad.objects.get(id=ad['id']).myClicks.count(), 3)
#             else:
#                 avg = 0
#             print('avg seconds:' + str(avg))
#             str_avg_time = str(timedelta(s00econds=avg))
#             print(str_avg_time)

#     # print(groups)
#     # print(objs)
#     # since groups is an iterator and not a list you have not yet traversed the list
    
#     # print(Click.objects.all().aggregate(avg_diff=Avg(F('date')-F('date'))))
#     # q1 = Click.objects.select_related('adID')
#     # q2 = View.objects.select_related('adID')
#     # print(q1.values('ip','adID__id','date').intersection(q2.values('ip', 'adID__id', 'date')))

#     # clicks = Click.objects.all()

#     # def date_hour(a,b):
#     #     e = a.strftime("%H")
#     #     ee = b.strftime("%H")
#     #     print(ee-e)

#     # for c in clicks:
#     #     view = View.objects.filter(
#     #         adID = c.adID,
#     #         ip = c.ip
#     #     )

#     #     date_hour(c.date, view[0].date)
#         # s = 0
#         # for v in view:
#         #     s += abs(c.date - v.date)
        
#         # print(s)

#     return render(request, 'home.html')
