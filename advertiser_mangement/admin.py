from django.contrib import admin

from .models import Ad, Advertiser, Click, View, summaryShit

admin.site.register(Advertiser)

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ["title", "link", "advertiser"]
    list_filter=["approve"]
    search_fields = ["title"]

@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ["adID", "date", "ip"]

@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    list_display = ['viewID', 'date', 'ip']

@admin.register(summaryShit)
class summaryShitAdmin(admin.ModelAdmin):
    list_display = ['adID', 'date', 'count', 'view_or_click']
