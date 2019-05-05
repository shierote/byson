# Generated by Django 2.2.1 on 2019-05-05 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('project', models.CharField(max_length=250)),
                ('project_hex_color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('description', models.CharField(max_length=250)),
                ('start', models.DateTimeField(verbose_name='date started')),
                ('end', models.DateTimeField(verbose_name='date ended')),
                ('dur', models.IntegerField(default=0)),
                ('expected_dur', models.IntegerField(default=0)),
                ('gap_ratio', models.IntegerField(default=0)),
                ('pid', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toggls.Project')),
            ],
        ),
    ]