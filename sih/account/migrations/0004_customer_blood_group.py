# Generated by Django 2.2.1 on 2019-05-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190527_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='blood_group',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]