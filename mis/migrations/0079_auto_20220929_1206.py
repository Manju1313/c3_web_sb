# Generated by Django 3.2.4 on 2022-09-29 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
        ('mis', '0078_untrustdcpu_bcpu_untrusteducatinalenrichmentsupportprovided_untrustvlcpcmetting'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='untrustdcpu_bcpu',
            options={'verbose_name_plural': 'Untrust DCPU_BCPU'},
        ),
        migrations.CreateModel(
            name='UntrustParentVocationalTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Active'), (2, 'Inactive')], db_index=True, default=1)),
                ('server_created_on', models.DateTimeField(auto_now_add=True)),
                ('server_modified_on', models.DateTimeField(auto_now=True)),
                ('unique_id', models.IntegerField(blank=True, null=True)),
                ('name_of_block', models.CharField(blank=True, max_length=250, null=True)),
                ('name_of_panchayat', models.CharField(blank=True, max_length=250, null=True)),
                ('name_of_village', models.CharField(blank=True, max_length=250, null=True)),
                ('name_of_awc_code', models.CharField(blank=True, max_length=250, null=True)),
                ('parent_name', models.CharField(blank=True, max_length=250, null=True)),
                ('training_complated', models.CharField(blank=True, max_length=250, null=True)),
                ('placement_accepted', models.CharField(blank=True, max_length=250, null=True)),
                ('placement_offered', models.CharField(blank=True, max_length=250, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='createdmis_untrustparentvocationaltraining_related', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modifiedmis_untrustparentvocationaltraining_related', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sites.site')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mis.task')),
            ],
            options={
                'verbose_name_plural': 'Untrust Parent Vocational Training',
            },
        ),
    ]
