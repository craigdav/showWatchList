from django.db import models

# Create your models here.

class Show(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=20)
    
