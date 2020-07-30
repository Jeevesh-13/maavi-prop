from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Customers(models.Model):
    Name = models.CharField(max_length=100,primary_key=True,blank=False)
    Email = models.EmailField(blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)
