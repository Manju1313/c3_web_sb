# Generated by Django 3.2.4 on 2022-08-29 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application_masters', '0008_trainingsubject'),
        ('mis', '0040_auto_20220829_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='adolescentvocationaltraining',
            name='training_subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application_masters.trainingsubject'),
        ),
    ]
