# Generated by Django 4.2.4 on 2023-10-06 08:20

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('luoghi', '0006_alter_place_descrizione_luogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='autore',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
