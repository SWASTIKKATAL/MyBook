from django.db import models

# Create your models here.
class Notes(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.TextField(null=False,max_length=30,blank= False)
    description = models.TextField()
    Query = models.TextField()
    