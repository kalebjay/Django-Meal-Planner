# Generated by Django 3.1.5 on 2021-03-03 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFood', '0011_auto_20210225_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='recipe',
        ),
        migrations.AddField(
            model_name='meal',
            name='recipe',
            field=models.ManyToManyField(null=True, to='appFood.Recipe'),
        ),
    ]
