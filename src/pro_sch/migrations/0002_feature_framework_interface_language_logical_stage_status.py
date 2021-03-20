# Generated by Django 3.1.7 on 2021-03-20 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pro_sch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Framework Name')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Language Name')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_development', models.CharField(choices=[('Init Project', 'Init Project'), ('Planning Process', 'Planning Process'), ('Design', 'Design'), ('Implementation', 'Implementation'), ('Testing', 'Testing'), ('Deploy', 'Deploy')], max_length=20, verbose_name='Development Stage')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pro_sch.project')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro_sch.status')),
            ],
        ),
        migrations.CreateModel(
            name='Logical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_name', models.CharField(max_length=25, unique=True, verbose_name='Database Name')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('framework', models.ManyToManyField(blank=True, to='pro_sch.Framework')),
                ('language', models.ManyToManyField(blank=True, to='pro_sch.Language')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pro_sch.project')),
            ],
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('framework', models.ManyToManyField(blank=True, to='pro_sch.Framework')),
                ('language', models.ManyToManyField(blank=True, to='pro_sch.Language')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pro_sch.project')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='DB Model Name')),
                ('oparetion', models.CharField(max_length=25, verbose_name='DB Model Oparetion')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Feature Notes')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pro_sch.project')),
            ],
        ),
    ]
