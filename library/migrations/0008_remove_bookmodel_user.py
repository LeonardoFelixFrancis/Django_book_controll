# Generated by Django 4.2.1 on 2023-05-17 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_bookmodel_start_reading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='user',
        ),
    ]
