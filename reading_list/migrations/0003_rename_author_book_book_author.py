# Generated by Django 3.2.8 on 2021-10-31 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reading_list', '0002_auto_20211026_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='book_author',
        ),
    ]
