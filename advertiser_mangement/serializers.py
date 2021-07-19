from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Ad, Advertiser

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('title', 'imgUrl', 'link', 'advertiser', 'approve')