# Generated by Django 3.2 on 2022-09-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
