# Generated by Django 2.2 on 2020-08-24 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0019_auto_20200818_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.Company'),
        ),
    ]
