# Generated by Django 4.1.6 on 2023-02-14 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='choice_description',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='text',
            new_name='description',
        ),
    ]
