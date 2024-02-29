from django.db import models

# Create your models here.
 

class Detail(models.Model):
   name=models.CharField(max_length=100)
   email=models.EmailField()
   tel=models.IntegerField(max_length=16)

   def __str__(self):
      return self.name