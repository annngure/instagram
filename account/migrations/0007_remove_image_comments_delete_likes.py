# Generated by Django 4.0.3 on 2022-03-09 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_likes_rename_profile_pic_profile_profile_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='comments',
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]