from django.db import models

class ShoppingList(models.Model):
    listName = models.CharField(max_length=50)
    note = models.CharField(max_length=50)
    isFavorite = models.BooleanField(default=False)