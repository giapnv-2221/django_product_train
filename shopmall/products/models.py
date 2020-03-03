from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField(max_length=400)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
