from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    employee_fullname = models.CharField(max_length=100)
    employee_code = models.CharField(max_length=25)
    employee_mobile = models.CharField(max_length=15)
    employee_position = models.ForeignKey(Position, on_delete=CASCADE)