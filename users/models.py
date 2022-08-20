from django.db import models

# Create your models here.
class Users(models.Model):
    Username = models.TextField()
    Password = models.TextField(null=False)
    