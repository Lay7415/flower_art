# Generated by Django 5.2 on 2025-04-13 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_courier_delivery_cor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='cor',
            new_name='courier',
        ),
    ]
