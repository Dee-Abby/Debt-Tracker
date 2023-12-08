from django.db import models

# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)





class Debt(models.Model):
    PAYMENT_STATUS = [
        
    ]
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    entity = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    date_borrowed = models.DateField(auto_created=True)