# Generated by Django 5.1.3 on 2024-11-28 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_status_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
    ]
