# Generated by Django 5.0.7 on 2024-08-02 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='likes'),
        ),
    ]
