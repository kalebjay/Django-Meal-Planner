# Generated by Django 3.1.5 on 2021-02-17 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFood', '0004_auto_20210214_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ManyToManyField(related_name='ingredients', to='appFood.Recipe'),
        ),
    ]
