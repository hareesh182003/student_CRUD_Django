# Generated by Django 5.0.7 on 2024-10-24 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('col_id', models.IntegerField(primary_key=True, serialize=False)),
                ('col_name', models.CharField(max_length=100)),
                ('col_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stu_name', models.CharField(max_length=40)),
                ('stu_year', models.IntegerField()),
                ('stu_address', models.CharField(max_length=50)),
                ('col_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.college')),
            ],
        ),
    ]