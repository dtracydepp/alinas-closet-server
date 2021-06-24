from django.db import models

class Piece(models.Model):
    piece_name = models.CharField(max_length=100)
    size =  models.CharField(max_length=50)
    imageurl =  models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    retailer =  models.ForeignKey("Retailer", on_delete=models.CASCADE)
    category =  models.ForeignKey("Category", on_delete=models.CASCADE)