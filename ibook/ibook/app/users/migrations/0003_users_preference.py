# Generated by Django 2.1.8 on 2020-04-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200424_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='preference',
            field=models.IntegerField(default='1'),
        ),
    ]
