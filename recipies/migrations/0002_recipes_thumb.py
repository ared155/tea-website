# Generated by Django 4.1.1 on 2022-09-12 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='thumb',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
