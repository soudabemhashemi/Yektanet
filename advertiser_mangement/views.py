from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Ad, Advertiser
from django.template import loader

# Create your views here.

def home(request):
    ad_list = Ad.objects.all()
    advertiser_list = Advertiser.objects.all()
    template = loader.get_template('home.html')
    context = {
        'ad_list': ad_list,
        'advertiser_list': advertiser_list,
    }
    print(context)
    return HttpResponse(template.render(context, request))

class HomePageView(TemplateView):
    template_name = 'home.html'

class AdPageView(TemplateView):
    template_name = 'ad1.html'

