# Generated by Django 4.2.6 on 2023-10-15 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_remove_music_vocabs_delete_vocab'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='voabulary',
            new_name='vocabulary',
        ),
    ]