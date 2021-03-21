# Generated by Django 3.1.7 on 2021-03-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210306_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bug',
            old_name='stepstoreproduce',
            new_name='steps_to_reproduce',
        ),
        migrations.AddField(
            model_name='bug',
            name='bug_priority',
            field=models.CharField(choices=[('P4', 'Low'), ('P3', 'Medium'), ('P2', 'High'), ('P1', 'Critical')], default='P4', max_length=2),
        ),
    ]
