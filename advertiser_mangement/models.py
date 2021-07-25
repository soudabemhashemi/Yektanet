from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return '{filename}'.format(filename=filename)


class Advertiser(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=200)
    imgUrl = models.ImageField(_("Image"), upload_to=upload_to)
    link = models.CharField(max_length=200)
    advertiser = models.ForeignKey(Advertiser(), on_delete=models.CASCADE, default=None, related_name="myAds")
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def countView(self, userIp):
        newView = View(viewID=self, ip=userIp)
        newView.save()

    def countClick(self, userIp):
        newClick = Click(adID=self, ip=userIp)
        newClick.save()


class Click(models.Model):
    adID = models.ForeignKey(Ad(), on_delete=models.CASCADE, blank=False, related_name="myClicks")
    date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()


class View(models.Model):
    viewID = models.ForeignKey(Ad(), on_delete=models.CASCADE, blank=False, related_name="myViews")
    date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()


class summaryShit(models.Model):
    adID = models.ForeignKey(Ad, on_delete=CASCADE, related_name="mySummary")
    date = models.DateTimeField()
    count = models.IntegerField()
    class Type(models.IntegerChoices):
        CLICK = 0
        VIEW = 1
    view_or_click = models.IntegerField(choices=Type.choices, default=1)
