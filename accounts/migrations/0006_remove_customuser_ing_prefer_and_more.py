# Generated by Django 5.0.4 on 2024-04-12 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_ingredients_ingredient_customuser_ing_prefer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='ing_prefer',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='ing_sensitive',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='skin_concerns',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='skin_type',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='SkinConcern',
        ),
    ]
