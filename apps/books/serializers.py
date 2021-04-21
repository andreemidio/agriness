from rest_framework import serializers

from apps.books.models import Books


class ListBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class PostBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['title']


class PutReserveBooksSerializer(serializers.Serializer):
    client_reserve = serializers.UUIDField()
