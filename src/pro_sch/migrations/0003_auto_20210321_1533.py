# Generated by Django 3.1.7 on 2021-03-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_sch', '0002_feature_framework_interface_language_logical_stage_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'get_latest_by': 'create_at', 'ordering': ['-create_at']},
        ),
        migrations.AlterField(
            model_name='framework',
            name='name',
            field=models.CharField(max_length=25, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=25, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='logical',
            name='db_name',
            field=models.CharField(max_length=25, verbose_name='Database Name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateField(verbose_name='Deadline'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Name'),
        ),
    ]
