# Generated by Django 4.2.5 on 2024-03-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usrpixeo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='optimized',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='images',
            name='remove_bg',
            field=models.BooleanField(default=False),
        ),
    ]
