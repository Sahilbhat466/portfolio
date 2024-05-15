from django.db import models

# Create your models here.

class Buy(models.Model):
    #Image 
    image = models.ImageField(upload_to = 'images/')
    #summary
    summary = models.CharField(max_length= 300)