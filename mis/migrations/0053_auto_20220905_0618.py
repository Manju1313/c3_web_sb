# Generated by Django 3.2.4 on 2022-09-05 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0052_auto_20220903_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participatingmeeting',
            name='department',
        ),
        migrations.RemoveField(
            model_name='participatingmeeting',
            name='type_of_meeting',
        ),
    ]