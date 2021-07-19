from django.urls import path
from django.urls.resolvers import URLPattern
from .views import AdAPIView

urlpatterns=[
    path('', AdAPIView.as_view()),
]