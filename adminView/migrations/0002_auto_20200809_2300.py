# Generated by Django 3.0.8 on 2020-08-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminView', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hajime',
            name='majors',
            field=models.CharField(choices=[('RPL', 'RPL'), ('TKJ', 'TKJ'), ('MM', 'MM')], default='RPL', max_length=20),
        ),
        migrations.AlterField(
            model_name='hajime',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hajime',
            name='name',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
