# Generated by Django 2.2 on 2020-08-18 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0018_auto_20200818_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='shops.Company'),
        ),
    ]
