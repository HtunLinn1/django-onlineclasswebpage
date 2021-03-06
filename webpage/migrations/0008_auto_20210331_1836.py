# Generated by Django 3.1.7 on 2021-03-31 09:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0007_auto_20210330_2112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['post_date']},
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 31, 18, 36, 40, 86681)),
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 31, 18, 36, 40, 86681)),
        ),
        migrations.CreateModel(
            name='CourseQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=1000)),
                ('start_date', models.DateTimeField(default=datetime.datetime(2021, 3, 31, 18, 36, 40, 87681))),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webpage.course', verbose_name='course')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webpage.registerstudent', verbose_name='student')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
    ]
