# Generated by Django 3.0.5 on 2020-12-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201228_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='foto',
            field=models.ImageField(default='', upload_to='media/'),
        ),
    ]
