# Generated by Django 3.2.21 on 2023-10-11 13:22

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_rename_original_bag_order_original_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
