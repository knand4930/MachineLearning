# Generated by Django 3.0.8 on 2020-07-04 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_news_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='time',
            field=models.CharField(default='00:00:00', max_length=8),
        ),
    ]