# Generated by Django 3.1.7 on 2021-03-21 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_sch', '0003_auto_20210321_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-create_at']},
        ),
    ]
