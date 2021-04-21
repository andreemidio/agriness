from django.urls import path, include
from rest_framework import routers

from apps.books.viewsets import ListBooksViewSet, PostBooksViewSet, PutReserveBooksViewSet

app_name = 'books'

router = routers.DefaultRouter()

router.register(r'books', ListBooksViewSet, basename='books')
router.register(r'books/add', PostBooksViewSet, basename='books-add')
router.register(r'books/reserve-book', PutReserveBooksViewSet, basename='reserve-book')

urlpatterns = [
    path(r'', include(router.urls)),

]
