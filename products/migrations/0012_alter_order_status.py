# Generated by Django 3.2 on 2022-09-22 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20220922_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
