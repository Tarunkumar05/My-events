# Generated by Django 3.2.19 on 2023-08-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_item_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
