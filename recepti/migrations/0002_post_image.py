# Generated by Django 3.0 on 2019-12-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepti', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media\\post_pics\\default.png', upload_to=''),
        ),
    ]
