# Generated by Django 3.2 on 2022-09-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20220924_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='stars',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
            preserve_default=False,
        ),
    ]
