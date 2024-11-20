# Generated by Django 5.1.2 on 2024-11-17 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('health_benefits', models.TextField()),
                ('common_location', models.CharField(max_length=200)),
            ],
        ),
    ]
