from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_ml = models.PositiveIntegerField()
    details = models.TextField()
    image = CloudinaryField('image')
    dealer_handle = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.quantity_ml}ml"