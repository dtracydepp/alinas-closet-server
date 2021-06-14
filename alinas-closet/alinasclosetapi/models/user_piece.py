from django.db import models

class UserPiece(models.Model):
    note = models.CharField(max_length=50)
    isFavorite = models.BooleanField(default=False)
    piece =  models.ForeignKey("Piece", null=True, blank = True, on_delete=models.CASCADE)
    user =  models.ForeignKey("User", on_delete=models.CASCADE)
    look =  models.ForeignKey("Look", null=True, blank = True, on_delete=models.CASCADE)
    shoppingList =  models.ForeignKey("shoppingList", on_delete=models.CASCADE)
