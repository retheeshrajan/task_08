# Generated by Django 2.0.4 on 2019-01-29 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='pic',
            new_name='logo',
        ),
    ]
