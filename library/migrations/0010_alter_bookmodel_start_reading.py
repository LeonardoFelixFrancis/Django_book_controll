# Generated by Django 4.2.1 on 2023-05-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_bookmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='start_reading',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]