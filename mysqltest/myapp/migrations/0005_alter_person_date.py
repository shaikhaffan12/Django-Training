# Generated by Django 4.0.5 on 2022-06-04 14:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_person_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]