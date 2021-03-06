# Generated by Django 3.0.5 on 2020-12-25 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='descripcion',
            field=models.CharField(max_length=10000, verbose_name='descripción'),
        ),
        migrations.AlterField(
            model_name='post',
            name='foto',
            field=models.ImageField(default='', upload_to='posts'),
        ),
    ]
