# Generated by Django 3.0.8 on 2020-07-05 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcat',
            name='catid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subcat',
            name='catname',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
