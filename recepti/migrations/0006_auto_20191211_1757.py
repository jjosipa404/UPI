# Generated by Django 3.0 on 2019-12-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepti', '0005_auto_20191210_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media\\post_pics\\default.jpg', upload_to='post_pics'),
        ),
    ]