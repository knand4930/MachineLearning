# Generated by Django 3.0.8 on 2020-07-05 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_news_ocatid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]