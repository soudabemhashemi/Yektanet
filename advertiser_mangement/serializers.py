from datetime import date
from django.db import models
from django.db.models import fields, indexes
from rest_framework import serializers, views
from .models import Ad, Advertiser, Click, View
from datetime import datetime



class AdSerializer(serializers.ModelSerializer):
    # imgUrl = serializers.ImageField(use_url=True, required=False, allow_empty_file=True)
    class Meta:
        model = Ad
        fields = ('title', 'link', 'imgUrl', 'advertiser')

class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = '__all__'

class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = '__all__'

    def create(self, validated_data):
        return View.objects.create(date=datetime.now())

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance
            

class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = ['name']