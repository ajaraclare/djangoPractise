from django.db import models

# Create your models here.

class test_table (models.Model):
    FirstName = models.CharField(max_length=20)
    Contact = models.IntegerField()
    Email = models.EmailField()

    def __str__(self):
        return self.FirstName