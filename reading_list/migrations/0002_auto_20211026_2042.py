# Generated by Django 3.2.8 on 2021-10-26 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]