# Generated by Django 3.0.8 on 2020-07-09 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_manager_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='email',
            field=models.TextField(),
        ),
    ]
