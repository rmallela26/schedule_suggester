# Generated by Django 4.2.13 on 2024-05-28 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='gpa',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]