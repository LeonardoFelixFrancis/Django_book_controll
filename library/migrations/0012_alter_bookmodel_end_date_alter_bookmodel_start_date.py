# Generated by Django 4.2.1 on 2023-05-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_alter_bookmodel_start_reading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
