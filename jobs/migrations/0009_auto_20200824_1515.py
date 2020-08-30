# Generated by Django 3.1 on 2020-08-24 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0008_auto_20200817_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='company',
        ),
        migrations.RemoveField(
            model_name='post',
            name='referral_id',
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('referral_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=30)),
                ('posts', models.ManyToManyField(to='jobs.post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
