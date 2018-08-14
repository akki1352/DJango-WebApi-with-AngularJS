from django.db import models

class employee(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
