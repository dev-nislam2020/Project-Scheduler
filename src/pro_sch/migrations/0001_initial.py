# Generated by Django 3.1.7 on 2021-03-20 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Project Name')),
                ('deadline', models.DateField(verbose_name='Project Deadline')),
                ('app_type', models.CharField(choices=[('Web', 'Web App Development'), ('Desktop', 'Desktop App Development'), ('Mobile', 'Mobile App Development'), ('Native', 'Native App Development')], max_length=20, verbose_name='Development')),
                ('is_completed', models.BooleanField(default=False)),
                ('is_requirement_completed', models.BooleanField(default=False)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-create_at'],
            },
        ),
    ]