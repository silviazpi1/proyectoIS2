# Generated by Django 3.0.5 on 2020-12-27 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201227_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='foto',
            field=models.ImageField(default='', upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateField(auto_now=True),
        ),
    ]
