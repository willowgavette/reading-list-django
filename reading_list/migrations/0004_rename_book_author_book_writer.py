# Generated by Django 3.2.8 on 2021-10-31 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reading_list', '0003_rename_author_book_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_author',
            new_name='writer',
        ),
    ]
