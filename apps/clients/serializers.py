from rest_framework import serializers

from apps.clients.models import Clients


class ListClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['id', 'fullname', 'cellphone', 'email']


class PostClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['id', 'fullname', 'cellphone', 'email']
