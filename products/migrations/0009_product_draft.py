# Generated by Django 5.0.4 on 2024-04-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='مشاهده'),
        ),
    ]
