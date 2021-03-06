# Generated by Django 3.1.7 on 2021-04-01 09:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webpage', '0009_auto_20210401_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursequestion',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 1, 18, 17, 42, 764970)),
        ),
        migrations.AlterField(
            model_name='coursespecialist',
            name='name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='course specialist'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 1, 18, 17, 42, 762970)),
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 1, 18, 17, 42, 763970)),
        ),
    ]
