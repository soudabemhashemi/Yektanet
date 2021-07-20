from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Ad, Advertiser, Click


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('title', 'imgUrl', 'link', 'advertiser', 'approve')

class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = '__all__'