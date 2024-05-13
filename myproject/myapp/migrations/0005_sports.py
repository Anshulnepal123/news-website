# Generated by Django 5.0.3 on 2024-04-10 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_newswrite_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('summary', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=True)),
            ],
        ),
    ]