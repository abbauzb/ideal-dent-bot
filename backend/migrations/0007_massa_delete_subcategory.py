# Generated by Django 4.1.4 on 2022-12-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_remove_product_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Massa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('massa', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]