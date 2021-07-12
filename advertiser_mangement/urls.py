from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ad1/', views.AdPageView.as_view(), name='ad1')
]