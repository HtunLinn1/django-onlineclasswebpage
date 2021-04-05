# Generated by Django 3.0.2 on 2021-04-03 10:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0012_auto_20210402_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursequestion',
            name='course',
            field=models.ForeignKey(default=0.1, on_delete=django.db.models.deletion.CASCADE, to='webpage.Course', verbose_name='course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursequestion',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 19, 16, 16, 700465)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 19, 16, 16, 700465)),
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='course',
            field=models.ForeignKey(default=0.1, on_delete=django.db.models.deletion.CASCADE, to='webpage.Course', verbose_name='course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 19, 16, 16, 700465)),
        ),
    ]