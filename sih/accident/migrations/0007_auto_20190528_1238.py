# Generated by Django 2.2.1 on 2019-05-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accident', '0006_auto_20190528_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='accident',
            name='acc_y',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accident',
            name='acc_z',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accident',
            name='angle_x',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accident',
            name='angle_y',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accident',
            name='angle_z',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]