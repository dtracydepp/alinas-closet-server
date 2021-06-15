from django.db import models
from django.contrib.auth.models import User

class UserPiece(models.Model):
    note = models.CharField(max_length=50)
    is_favorite = models.BooleanField(default=False)
    piece =  models.ForeignKey("Piece", on_delete=models.CASCADE)
    user =  models.ForeignKey( User, on_delete=models.CASCADE)
    look =  models.ForeignKey("Look", null=True, blank = True, on_delete=models.CASCADE)
    shopping_list =  models.ForeignKey("ShoppingList", null=True, blank = True, on_delete=models.CASCADE)
