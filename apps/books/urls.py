from django.urls import path, include
from rest_framework import routers

from apps.books.viewsets import ListBooksViewSet, PostBooksViewSet

app_name = 'books'

router = routers.DefaultRouter()

router.register(r'books', ListBooksViewSet, basename='books')
router.register(r'books/add', PostBooksViewSet, basename='books-add')

urlpatterns = [
    path(r'', include(router.urls)),
]
