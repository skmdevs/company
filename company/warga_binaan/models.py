from django.db import models

# Create your models here.
class Prison(models.Model):
    no_reg = models.CharField(max_length=25)
    nama = models.CharField(max_length=100)
    pasal = models.CharField(max_length=100)
    hukuman = models.CharField(max_length=100)
    prisoner_status = models.CharField(max_length=25)