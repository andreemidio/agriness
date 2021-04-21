from rest_framework import mixins, renderers, parsers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.books.models import Books
from apps.clients.models import Clients
from apps.clients.serializers import ListClientsSerializer, PostClientsSerializer


class ListClientsViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Clients.objects.all()
    serializer_class = ListClientsSerializer
    renderer_classes = (renderers.JSONRenderer,)
    parser_classes = (parsers.JSONParser,)

    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        data = Books.objects.filter(client_reserve=pk).values()

        return Response(data, status.HTTP_200_OK)


class PostClientsViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Clients.objects.all()
    serializer_class = PostClientsSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.StaticHTMLRenderer, renderers.TemplateHTMLRenderer,)
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser,)
