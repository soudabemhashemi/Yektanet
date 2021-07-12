from django import template
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Ad, Advertiser
from django.template import loader

from django.views.generic.base import RedirectView

from django.shortcuts import redirect
# class AdCounterClicksRedirectView(RedirectView):

#     query_string = True
#     pattern_name = 'article-detail'

#     def get_redirect_url(self, *args, **kwargs):
#         adClicks = get_object_or_404(Ad, pk=kwargs['pk'])
#         adClicks.update_counter()
#         return super().get_redirect_url(*args, **kwargs)

def home(request):
    ad_list = Ad.objects.all()
    advertiser_list = Advertiser.objects.all()
    template = loader.get_template('home.html')
    context = {
        'ad_list': ad_list,
        'advertiser_list': advertiser_list,
    }
    return HttpResponse(template.render(context, request))


def countClicks(request):
    print("____________________________________________________")
    print(request)
    return redirect('home')

class createAd(CreateView):
    model = Ad
    template_name = 'create_new.html'
    fields = '__all__'

