# Generated by Django 4.0.dev20210712094637 on 2021-07-12 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_mangement', '0005_alter_ad_clicks_alter_ad_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertiser',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='advertiser',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]