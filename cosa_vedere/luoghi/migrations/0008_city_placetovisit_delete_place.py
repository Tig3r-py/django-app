# Generated by Django 4.2.4 on 2023-10-07 08:12

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luoghi', '0007_alter_place_autore'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_luogo', models.CharField(max_length=50)),
                ('immagine', models.ImageField(upload_to='')),
                ('autore', ckeditor_uploader.fields.RichTextUploadingField()),
                ('descrizione_luogo', ckeditor_uploader.fields.RichTextUploadingField()),
                ('citta', models.BooleanField(default=True)),
                ('sintesi', models.TextField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceToVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('immagine', models.ImageField(upload_to='')),
                ('autore', ckeditor_uploader.fields.RichTextUploadingField()),
                ('descrizione_luogo', ckeditor_uploader.fields.RichTextUploadingField()),
                ('prezzo', models.FloatField(blank=True)),
                ('dove', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='luoghi.city')),
            ],
        ),
        migrations.DeleteModel(
            name='Place',
        ),
    ]