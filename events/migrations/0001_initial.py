# Generated by Django 3.2.19 on 2023-08-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_price', models.IntegerField()),
                ('item_location', models.CharField(max_length=200)),
                ('item_description', models.CharField(max_length=200)),
                ('item_category', models.CharField(max_length=200)),
            ],
        ),
    ]