# Generated by Django 3.2.8 on 2022-02-22 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_rename_contactsform_contactsformmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactsFormModel',
            new_name='ContactForm',
        ),
        migrations.RemoveField(
            model_name='serviceform',
            name='file',
        ),
    ]
