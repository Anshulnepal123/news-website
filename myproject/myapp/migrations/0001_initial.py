# Generated by Django 5.0.3 on 2024-04-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newswrite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
