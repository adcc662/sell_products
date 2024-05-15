from django.db import models
from apps.products.models import Products


class Inventory(models.Model):
    """
    Inventory model
    """
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    TYPE_CHOICES = (
        ('IN', 'Input'),
        ('OUT', 'Output')
    )
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.type}"
