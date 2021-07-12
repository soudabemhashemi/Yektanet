from django.db import models
# Create your models here.

class Advertiser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    # clicks = IntegerField()
    # views = IntegerField()


class Ad(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    imgUrl = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    clicks = models.IntegerField()
    views = models.IntegerField()
