# Generated by Django 4.0.dev20210715050039 on 2021-07-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_mangement', '0012_remove_advertiser_clicks_remove_advertiser_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='view',
            name='a',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]