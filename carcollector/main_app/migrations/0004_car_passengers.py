# Generated by Django 4.0.4 on 2022-04-27 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_car_passengers'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='passengers',
            field=models.ManyToManyField(to='main_app.passenger'),
        ),
    ]
