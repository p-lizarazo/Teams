# Generated by Django 2.1.3 on 2018-11-19 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20181119_0326'),
        ('team', '0002_team_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='dashboards',
            field=models.ManyToManyField(to='dashboard.Board'),
        ),
    ]
