from django.db import models

# Create your models here.

class Info (models.Model):
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name
