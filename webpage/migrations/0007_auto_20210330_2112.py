# Generated by Django 3.0.2 on 2021-03-30 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0006_auto_20210329_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 30, 21, 12, 56, 119387)),
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 30, 21, 12, 56, 120405)),
        ),
    ]
