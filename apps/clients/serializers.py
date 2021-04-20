from rest_framework import serializers

from apps.clients.models import Clients


class ListClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


# class ListBooksClientsSerializer(se)