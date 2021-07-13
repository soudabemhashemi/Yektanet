from django.db import models
from django.urls import reverse

class Advertiser(models.Model):
    name = models.CharField(max_length=200)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)


class Ad(models.Model):
    title = models.CharField(max_length=200)
    imgUrl = models.ImageField()
    clicks = models.IntegerField(default=0, blank=True)
    views = models.IntegerField(default=0, blank=True)
    link = models.CharField(max_length=200)
    advertiser = models.ForeignKey(Advertiser(), on_delete=models.CASCADE, default=None)

# class Click(models.Model):
#     adID = models.ForeignKey(Ad(), on_delete=models.CASCADE, blank=False)
#     date = models.DateField()

# class View(models.Model):
#     viewID = models.ForeignKey(Ad(), on_delete=models.CASCADE, blank=False)
#     date = models.DateField()
