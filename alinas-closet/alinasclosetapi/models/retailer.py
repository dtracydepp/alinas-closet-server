from django.db import models

class Retailer(models.Model):
    retailer_name = models.CharField(max_length=50)