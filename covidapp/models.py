from django.db import models
from django_countries.fields import CountryField
# Create your models here.
class Countries(models.Model):
    country=CountryField()
    
    