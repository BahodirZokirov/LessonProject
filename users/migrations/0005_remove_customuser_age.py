# Generated by Django 5.0.3 on 2024-03-29 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
    ]
