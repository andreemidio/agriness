from rest_framework import mixins, renderers, parsers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.books.models import Books
from apps.books.serializers import ListBooksSerializer, PostBookSerializer, PutReserveBooksSerializer


class ListBooksViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Books.objects.all()
    serializer_class = ListBooksSerializer
    renderer_classes = (renderers.JSONRenderer,)
    parser_classes = (parsers.JSONParser,)

    @action(detail=True, methods=['get'])
    def reserve(self, request, pk=None):
        self.queryset.filter(id=pk).update(is_reserve=True)

        content = dict(
            info='Reserva efetuada com sucesso'
        )

        return Response(content, status.HTTP_200_OK)


class PostBooksViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Books.objects.all()
    serializer_class = PostBookSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.StaticHTMLRenderer, renderers.TemplateHTMLRenderer]
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser,)


class PutReserveBooksViewSet(mixins.UpdateModelMixin, GenericViewSet):
    queryset = Books.objects.all()
    serializer_class = PutReserveBooksSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.StaticHTMLRenderer, renderers.TemplateHTMLRenderer)
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser,)

    def update(self, request, *args, **kwargs):
        self.queryset.update(is_reserve=True, client_reserve=request.data['client_reserve'])

        content = dict(
            info=f'Reserva efetuada com sucesso para o usuario '
        )

        return Response(content, status.HTTP_200_OK)
