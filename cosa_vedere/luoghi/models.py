from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class City(models.Model):
    nome_luogo = models.CharField(max_length=50)
    immagine = models.ImageField()
    autore = RichTextUploadingField()
    descrizione_luogo = RichTextUploadingField()
    citta = models.BooleanField(default=True)
    sintesi = models.TextField(max_length=2000, blank=True)
    #dove = models.CharField(max_length=30, blank=True)
    
    def check_luoghi(self):
        super.check()
        if self.citta and not self.sintesi:
            raise ValidationError("completare mettere una breve descrizione")
        elif not self.citta and not self.dove:
            raise ValidationError("scrivere dov'è la città")
        
    def __str__(self):
        return self.nome_luogo
    
class PlaceToVisit(models.Model):
    dove = models.ForeignKey(City, default=None, on_delete=models.CASCADE) #models.SET_NULL,      null =True
    nome = models.CharField(max_length=50)
    immagine = models.ImageField()
    immagine_45 = models.ImageField()
    autore = RichTextUploadingField()
    descrizione = RichTextUploadingField()
    prezzo = models.FloatField(blank=True)
    storia = RichTextUploadingField()
    riassunto = RichTextUploadingField()
    mappa = RichTextUploadingField()
    #mettere approfondimenti e una immagine che sia in 4:5 e una più larga

    def __str__(self):
        return self.nome
    
    class Meta:
      ordering = ['-dove']