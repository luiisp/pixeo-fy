# Generated by Django 4.2.5 on 2024-03-29 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usrpixeo', '0002_images_optimized_images_remove_bg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='optimized',
            field=models.BooleanField(default=False),
        ),
    ]
