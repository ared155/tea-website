# Generated by Django 4.1.1 on 2022-09-16 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(default=str, max_length=100),
        ),
    ]
