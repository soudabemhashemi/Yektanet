from django.shortcuts import render
from rest_framework import generics
from advertiser_mangement.models import Ad, Advertiser
from .serializers import AdSerializer

class AdAPIView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer