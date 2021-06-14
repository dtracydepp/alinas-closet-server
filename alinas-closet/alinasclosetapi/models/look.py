from django.db import models

class Look(models.Model):
    lookName = models.CharField(max_length=50)
    note = models.CharField(max_length=50)