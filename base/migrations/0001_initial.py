# Generated by Django 5.0.6 on 2024-06-17 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Table',
            },
        ),
    ]
