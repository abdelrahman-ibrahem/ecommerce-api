# Generated by Django 3.2 on 2022-09-22 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20220922_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='products',
            new_name='product',
        ),
    ]
