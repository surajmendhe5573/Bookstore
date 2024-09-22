from django.urls import path
from .views import *
urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('create/', BookCreateView.as_view(), name='book-create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    path('<int:book_id>/add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('<int:book_id>/remove-from-cart/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('cart/', ViewCartView.as_view(), name='view-cart'),
]
