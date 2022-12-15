# Generated by Django 3.2.4 on 2022-07-14 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mis', '0015_auto_20220714_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='facedrelatedoperation',
            name='user_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='facedrelatedoperation',
            name='challenges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='facedrelatedoperation',
            name='proposed_solution',
            field=models.TextField(blank=True, null=True),
        ),
    ]
