# Generated by Django 2.1.1 on 2018-10-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, unique=True)),
                ('last_name', models.CharField(max_length=255, unique=True)),
                ('email', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]