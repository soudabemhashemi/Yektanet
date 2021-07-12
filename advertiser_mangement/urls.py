from django.urls import path

from . import views

# app_name = 'advertiser_mangement'

urlpatterns = [
    path('', views.home, name='home'),
    path('countClicks', views.countClicks, name='countClicks'),
    path('create/new/', views.createAd.as_view(), name='create_new')
]