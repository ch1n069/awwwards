# Generated by Django 4.0.5 on 2022-06-15 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0008_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_photo',
            new_name='photo',
        ),
    ]