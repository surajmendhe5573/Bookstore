from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
# cart model

from django.conf import settings
from django.db import models
from books.models import Book  # Adjust import based on your structure

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'book')  # Prevent multiple entries for the same book

    def __str__(self):
        return f"{self.user.username}'s cart: {self.book.title} (Quantity: {self.quantity})"
