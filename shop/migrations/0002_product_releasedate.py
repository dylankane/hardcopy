# Generated by Django 3.2.21 on 2023-10-02 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='releasedate',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
