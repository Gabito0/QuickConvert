from django.db import models

class DataSource(models.Model):
  soure_id= models.AutoField(primary_key=True, blank=False)
  name = models.CharField(max_length=200, blank=False)
  description = models.TextField(blank=False) 
  source_type = models.CharField(max_length=50,blank=False)

class DataEntry(models.Model):
  class Status(models.TextChoices):
    PENDING = 'PD', 'Pending'
    FINISHED = 'FN', 'Finished'
    ERROR = 'ER', 'ERROR'
  entry_id = models.AutoField(primary_key=True,blank=False)
  source_id = models.ForeignKey(DataSource, on_delete=models.CASCADE)
  received_at = models.DateTimeField(auto_now=True,blank=False)
  status = models.CharField(max_length=2, choices=Status.choices, default= Status.PENDING)
  updated_at = models.DateTimeField(auto_now=True)


class NormalizeData(models.Model):
  data_id = models.AutoField(primary_key=True, blank=False)
  entry_id = models.ForeignKey(DataEntry, on_delete=models.CASCADE)
  company_name = models.CharField(max_length=200, blank=False)
  location = models.CharField(blank=False, max_length=300)
  product = models.CharField(blank=False, max_length=200)
  quantity = models.IntegerField(blank=None)
  price = models.IntegerField(blank=None)


