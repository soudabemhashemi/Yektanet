# Generated by Django 4.0.dev20210712094637 on 2021-07-13 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_mangement', '0009_remove_ad_clicks_remove_ad_views_view_click'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]
