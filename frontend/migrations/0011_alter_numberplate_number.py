# Generated by Django 4.0.2 on 2022-02-17 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0010_image_video_delete_mediafiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberplate',
            name='number',
            field=models.CharField(max_length=15),
        ),
    ]
