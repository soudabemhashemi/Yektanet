# Generated by Django 4.0.dev20210712094637 on 2021-07-12 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_mangement', '0004_alter_ad_clicks_alter_ad_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='clicks',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
