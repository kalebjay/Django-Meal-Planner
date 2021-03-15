# Generated by Django 3.1.5 on 2021-03-03 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appFood', '0012_auto_20210302_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='recipe',
        ),
        migrations.AddField(
            model_name='meal',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appFood.recipe'),
        ),
    ]
