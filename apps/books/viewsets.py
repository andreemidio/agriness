from rest_framework import mixins, renderers, parsers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.books.models import Books
from apps.books.serializers import ListBooksSerializer, PostBookSerializer


class ListBooksViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Books.objects.all()
    serializer_class = ListBooksSerializer
    renderer_classes = [renderers.StaticHTMLRenderer, renderers.TemplateHTMLRenderer, renderers.JSONRenderer]
    parser_classes = (parsers.MultiPartParser,)

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
    renderer_classes = [renderers.StaticHTMLRenderer, renderers.TemplateHTMLRenderer, renderers.JSONRenderer]
    parser_classes = (parsers.MultiPartParser,)
