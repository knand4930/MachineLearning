# Generated by Django 3.0.8 on 2020-07-07 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20200706_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.TextField(default=''),
        ),
    ]
