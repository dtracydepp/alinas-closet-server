from django.db import models

class ShoppingList(models.Model):
    list_name = models.CharField(max_length=50)
    note = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)