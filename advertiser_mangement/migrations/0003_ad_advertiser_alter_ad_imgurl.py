# Generated by Django 4.0.dev20210712094637 on 2021-07-12 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_mangement', '0002_alter_ad_id_alter_advertiser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='advertiser',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='advertiser_mangement.advertiser'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='imgUrl',
            field=models.ImageField(upload_to=''),
        ),
    ]
