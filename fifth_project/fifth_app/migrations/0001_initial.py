# Generated by Django 2.1.1 on 2018-10-20 18:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('portfolio_pic', models.ImageField(blank=True, upload_to='profile_pic')),
                ('user', models.OneToOneField(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
