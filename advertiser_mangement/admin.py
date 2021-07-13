from django.contrib import admin

from .models import Ad, Advertiser, Click, View

# admin.site.register(Ad)
admin.site.register(Advertiser)
admin.site.register(View)
# class AdAdmin(admin.ModelAdmin):
#     list_display = ["title", "link"]
#     list_filter=["approve"]
#     search_fields = ["title", "clicks"]

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ["title", "link", "advertiser"]
    list_filter=["approve"]
    search_fields = ["title"]

@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ["adID", "date", "ip"]
