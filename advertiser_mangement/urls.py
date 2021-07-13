from django.urls import path
from . import views

app_name = 'advertiser_mangement'

urlpatterns = [
    path('', views.home, name='home'),
    path('countClicks/<int:pk>/', views.countClicks.as_view(), name='countClicks'),
    path('create_new/', views.createAd, name='create_new')
]