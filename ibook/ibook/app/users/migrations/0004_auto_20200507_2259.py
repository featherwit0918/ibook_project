# Generated by Django 2.1.8 on 2020-05-07 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_preference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='token',
        ),
        migrations.AddField(
            model_name='users',
            name='headimage',
            field=models.CharField(default='', max_length=128, null=True),
        ),
    ]