from django.urls import path
from . import views


app_name = 'advertiser_mangement'

urlpatterns = [
    # path('', views.AdList.as_view(), name='home'),
    path('createAd/', views.createAd.as_view(), name='create_new'),
    path('createAdvertiser/', views.createAdvertiser, name='createSdvertiser'), 
    # path('create_new/create_new/', views.createAd.as_view(), name='create_new'),
    # path('countClicks/<int:pk>/', views.countClicks.as_view(), name='countClicks'),
    # path('report/', views.report, name='report')
]

