# Generated by Django 3.1.7 on 2021-03-07 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210307_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 7, 17, 44, 26, 800461)),
        ),
    ]