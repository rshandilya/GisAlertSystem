# Generated by Django 2.2.1 on 2019-05-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accidents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=7, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=7, max_digits=9)),
                ('occurrence', models.DateTimeField()),
                ('status', models.CharField(choices=[('DET', 'Detect'), ('ACK', 'Acknowledge'), ('CNF', 'Confirm')], default='DET', max_length=5)),
            ],
        ),
    ]
