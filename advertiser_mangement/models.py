from django.db import models
# Create your models here.

class Advertiser(models.Model):
    name = models.CharField(max_length=200)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)


class Ad(models.Model):
    title = models.CharField(max_length=200)
    imgUrl = models.ImageField()
    link = models.CharField(max_length=200)
    clicks = models.IntegerField(default=0, blank=True, null=True)
    views = models.IntegerField(default=0, blank=True, null=True)
    advertiser = models.ForeignKey(Advertiser(), on_delete=models.CASCADE, default=None)


