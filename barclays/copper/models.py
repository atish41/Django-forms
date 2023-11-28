from django.db import models

# Create your models here.
class copperProduct(models.Model):
    prd_name=models.CharField(max_length=25)
    prd_qnty=models.IntegerField()
    prd_validity=models.BooleanField(default=False)
    prd_valid_upto=models.DateField()
