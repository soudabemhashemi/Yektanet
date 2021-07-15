from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse

class Advertiser(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=200)
    imgUrl = models.ImageField()
    link = models.CharField(max_length=200)
    advertiser = models.ForeignKey(Advertiser(), on_delete=models.CASCADE, default=None)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Click(models.Model):
    adID = models.ForeignKey(Ad(), on_delete=models.CASCADE, blank=False, related_name="myClicks")
    date = models.DateTimeField()
    ip = models.GenericIPAddressField()

class View(models.Model):
    viewID = models.ForeignKey(Ad(), on_delete=models.CASCADE, blank=False, related_name="myViews")
    date = models.DateTimeField()
    ip = models.GenericIPAddressField()