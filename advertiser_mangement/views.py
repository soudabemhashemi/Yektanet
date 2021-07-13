from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Ad, Advertiser
from django.template import loader

from django.views.generic.base import RedirectView

from django.shortcuts import redirect

def home(request):
    ad_list = Ad.objects.all()
    advertiser_list = Advertiser.objects.all()
    template = loader.get_template('home.html')
    context = {
        'ad_list': ad_list,
        'advertiser_list': advertiser_list,
    }
    return HttpResponse(template.render(context, request))


class countClicks(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        ad = Ad.objects.get(pk=kwargs['pk'])
        ad.clicks = ad.clicks +1
        ad.save()
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

