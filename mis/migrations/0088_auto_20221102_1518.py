# Generated by Django 3.2.4 on 2022-11-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0087_auto_20221102_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adolescentre_enrolled',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='adolescentre_enrolled',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True),
        ),
        migrations.AlterField(
            model_name='parentvocationaltraining',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
