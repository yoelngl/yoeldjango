# Generated by Django 3.0.8 on 2020-08-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminView', '0004_auto_20200809_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hajime',
            name='majors',
            field=models.CharField(max_length=100),
        ),
    ]
