# Generated by Django 3.2.4 on 2022-07-20 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0024_auto_20220720_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='boysahwd',
            name='date_of_ahwd',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='girlsahwd',
            name='date_of_ahwd',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sessionmonitoring',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
