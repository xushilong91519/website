from django.db import models
from django.utils import timezone

# Create your models here.

class Order(models.Model):
    order_number=models.CharField(max_length=200)
    customer_code=models.CharField(max_length=200)
    order_date=models.DateTimeField('date ordered')
    assign_date=models.DateTimeField('date assigned')
    survey_locations=models.CharField(max_length=200)
    depot_code=models.CharField(max_length=200)
    depot_name=models.CharField(max_length=200)
    unit_type=models.CharField(max_length=200)
    qty=models.IntegerField()
    release_number=models.CharField(max_length=200)
    container_number=models.CharField(max_length=200)
    survey_code=models.CharField(max_length=200)
    remark=models.TextField()

    def __str__(self):
        return self.order_number
