# Generated by Django 3.2.4 on 2022-09-02 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_masters', '0011_auto_20220902_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adolescent',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')]),
        ),
    ]