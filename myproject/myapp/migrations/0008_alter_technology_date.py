# Generated by Django 5.0.3 on 2024-04-11 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
