# Generated by Django 5.0.6 on 2024-06-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_menu_alter_table_capacity_alter_table_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name_plural': 'Menu'},
        ),
    ]
