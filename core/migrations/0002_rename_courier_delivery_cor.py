# Generated by Django 5.2 on 2025-04-13 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='courier',
            new_name='cor',
        ),
    ]
