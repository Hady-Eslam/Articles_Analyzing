# Generated by Django 2.1.3 on 2018-12-18 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0010_likes_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='Status',
            new_name='Deleted',
        ),
    ]