# Generated by Django 4.1.4 on 2022-12-26 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_alter_subcategory_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='color',
        ),
    ]
