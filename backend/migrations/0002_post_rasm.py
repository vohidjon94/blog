# Generated by Django 4.0.3 on 2022-04-14 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rasm',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
