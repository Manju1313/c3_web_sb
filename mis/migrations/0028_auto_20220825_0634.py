# Generated by Django 3.2.4 on 2022-08-25 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0027_rename_seconf_inst_visited_champions_second_inst_visited'),
    ]

    operations = [
        migrations.AddField(
            model_name='ahsession',
            name='session_day',
            field=models.IntegerField(blank=True, choices=[(1, 'Day-1'), (2, 'Day-2'), (3, 'Day-3')], null=True),
        ),
        migrations.AddField(
            model_name='dlsession',
            name='session_day',
            field=models.IntegerField(blank=True, choices=[(1, 'Day-1'), (2, 'Day-2'), (3, 'Day-3')], null=True),
        ),
    ]
