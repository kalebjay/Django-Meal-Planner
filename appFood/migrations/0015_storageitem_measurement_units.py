# Generated by Django 3.1.5 on 2021-03-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFood', '0014_auto_20210304_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='storageitem',
            name='measurement_units',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
