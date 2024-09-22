from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]


# cart 
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart
from .serializers import CartSerializer

class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_id):
        user = request.user
        quantity = request.data.get('quantity', 1)
        cart_item, created = Cart.objects.get_or_create(
            user=user, 
            book_id=book_id,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity  # Increment if exists
            cart_item.save()
        
        return Response(CartSerializer(cart_item).data, status=201)

class RemoveFromCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, book_id):
        user = request.user
        try:
            cart_item = Cart.objects.get(user=user, book_id=book_id)
            cart_item.delete()
            return Response({"detail": "Book removed from cart."}, status=204)
        except Cart.DoesNotExist:
            return Response({"detail": "Cart item not found."}, status=404)

class ViewCartView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
