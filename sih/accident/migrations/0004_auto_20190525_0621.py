# Generated by Django 2.2.1 on 2019-05-25 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accident', '0003_auto_20190525_0430'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Accidents',
            new_name='Accident',
        ),
    ]
