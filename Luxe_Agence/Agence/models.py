from django.db import models

# Create your models here.

class Residence(models.Model):
    image = models.ImageField(upload_to='residence_images/')
    nomResidence = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nomResidence
    
