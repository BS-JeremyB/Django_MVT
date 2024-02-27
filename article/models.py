from django.db import models

# Create your models here.

class Article (models.Model):
    titre = models.CharField(max_length=150)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)