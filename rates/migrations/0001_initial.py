# Generated by Django 5.0.1 on 2024-01-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FxRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(max_length=24)),
                ('date_of_query', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
