# Generated by Django 3.1.7 on 2021-04-03 10:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0013_auto_20210403_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursequestion',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 19, 53, 4, 956815)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.coursespecialist'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 19, 53, 4, 941130)),
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 19, 53, 4, 956815)),
        ),
    ]
