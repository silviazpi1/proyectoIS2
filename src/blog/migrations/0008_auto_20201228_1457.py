# Generated by Django 3.0.5 on 2020-12-28 14:57

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201227_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='descripcion',
            field=djrichtextfield.models.RichTextField(verbose_name='descripción'),
        ),
    ]
