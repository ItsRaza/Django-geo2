# Generated by Django 2.2.5 on 2020-08-11 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0006_auto_20200811_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='location',
        ),
    ]
