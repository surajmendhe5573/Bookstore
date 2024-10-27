from rest_framework import serializers
from .models import *

# book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'price', 'stock']

# cart 
class CartSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(source='book.title', read_only=True)  # Assuming the Book model has a 'title' field
    author = serializers.CharField(source='book.author', read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ['user', 'author']