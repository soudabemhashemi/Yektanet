from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Ad, Advertiser, Click, View
from django.template import loader
from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import redirect
from django.template.response import TemplateResponse
import datetime

# def home(request):
#     ad_list = Ad.objects.all()
#     advertiser_list = Advertiser.objects.all()
#     template = loader.get_template('home.html')
#     context = {
#         'ad_list': ad_list,
#         'advertiser_list': advertiser_list,
#     }
#     return HttpResponse(template.render(context, request))

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad_list'] = Ad.objects.all()
        context['advertiser_list'] = Advertiser.objects.all()
        return context

class countClicks(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        ad = Ad.objects.get(pk=kwargs['pk'])
        # ad.clicks = ad.clicks +1
        # ad.views = ad.views +1
        newClick = Click(adID=ad, date=datetime.datetime.now().today(), ip='8181')
        newClick.save()
        # newView = View(viewID=ad, date=datetime.datetime.now(), ip='8181')
        # newView.save()
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

