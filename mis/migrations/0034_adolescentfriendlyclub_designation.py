# Generated by Django 3.2.4 on 2022-08-29 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0033_remove_adolescentfriendlyclub_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='adolescentfriendlyclub',
            name='designation',
            field=models.IntegerField(blank=True, choices=[(1, 'ANM'), (2, 'Sahiya'), (3, 'Sevika'), (4, 'Peer Educator'), (5, 'Cluster Coordinator'), (6, 'Project Officer'), (7, 'SPO'), (8, 'Others')], null=True),
        ),
    ]
