from django.db import models

# Create your models here.
class DataSources(models.Model):
  soure_id= models.TextField(primary_key=True)
  name = models.CharField(max_length=200, blank=False)
  description = models.TextField(blank=False) 
  source_type = models.CharField(max_length=50,blank=False)