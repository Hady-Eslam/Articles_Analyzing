# Generated by Django 2.1.3 on 2018-12-01 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='Picture',
            field=models.CharField(default='None', max_length=100),
        ),
    ]