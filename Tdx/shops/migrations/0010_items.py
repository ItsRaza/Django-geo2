# Generated by Django 2.2 on 2020-08-17 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0009_auto_20200814_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='item', max_length=200)),
                ('belonging_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.Shop')),
            ],
        ),
    ]
