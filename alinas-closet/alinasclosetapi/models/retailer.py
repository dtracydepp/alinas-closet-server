from django.db import models

class Retailer(models.Model):
    retailerName = models.CharField(max_length=50)