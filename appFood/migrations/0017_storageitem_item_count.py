# Generated by Django 3.1.5 on 2021-03-08 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFood', '0016_auto_20210308_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='storageitem',
            name='item_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
