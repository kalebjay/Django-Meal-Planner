# Generated by Django 3.1.5 on 2021-02-25 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFood', '0010_auto_20210222_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storageitem',
            name='quant_onHand',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
