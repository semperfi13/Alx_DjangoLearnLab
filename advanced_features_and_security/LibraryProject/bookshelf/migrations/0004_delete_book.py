# Generated by Django 5.1.6 on 2025-02-15 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0003_remove_book_publication_year'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
