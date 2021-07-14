from django import template
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
from django.db.models import Count
# from advertiser_mangement.middleware import getIPMiddleware

# def home(request):
#     ad_list = Ad.objects.all()
#     advertiser_list = Advertiser.objects.all()
#     template = loader.get_template('home.html')
#     context = {
#         'ad_list': ad_list,
#         'advertiser_list': advertiser_list,
#     }
#     return HttpResponse(template.render(context, request))
def countViews(request, post_ids):
    for post_id in post_ids:
        ad = Ad.objects.get(id = post_id.id)
        ip = getIP(request)
        newView = View(viewID=ad, date=datetime.datetime.now(), ip=ip)
        newView.save()

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad_list'] = Ad.objects.all()
        context['advertiser_list'] = Advertiser.objects.all()
        countViews(self.request, context['ad_list'])
        return context

class countClicks(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        ad = Ad.objects.get(pk=kwargs['pk'])
        ip = getIP(self.request)
        newClick = Click(adID=ad, date=datetime.datetime.now().today(), ip=ip)
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


def getIP(request):
    x_firwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_firwarded_for:
        ip = x_firwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def report(request):
    print(Click.objects.values('adID', entries=Count('date.now')))
