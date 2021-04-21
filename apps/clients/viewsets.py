from datetime import date
from datetime import datetime

from rest_framework import mixins, renderers, parsers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.books.models import Books
from apps.books.serializers import ListBooksSerializer
from apps.clients.models import Clients
from apps.clients.serializers import ListClientsSerializer, PostClientsSerializer


class ListClientsViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Clients.objects.all()
    serializer_class = ListClientsSerializer
    renderer_classes = (renderers.JSONRenderer,)
    parser_classes = (parsers.JSONParser,)

    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        data = Books.objects.filter(client_reserve=pk)

        serializer = ListBooksSerializer(instance=data, many=True)

        values = serializer.data

        now = date.today()

        result = list()

        for i in values:
            data_devolution = i['date_devolution']
            date_time_obj = datetime.strptime(data_devolution, '%Y-%m-%d').date()

            duration = (now - date_time_obj)
            duration = duration.days

            delay_time = dict()

            if duration == 0:
                delay_time.update(
                    dict(
                        atraso='Sem Atraso'
                    )
                )

            elif duration <= 3:
                delay_time.update(
                    dict(
                        atraso='Atraso de até 3 dias ',
                        multa='3%',
                        juros_dia='0.2% ao dia ',
                        acumulado=f'{duration * 0.2}% de juros acumulado'
                    )
                )

            elif duration > 3 and duration <= 5:
                delay_time.update(
                    dict(
                        atraso='Atraso entre 3 a 5 dias ',
                        multa='5% ',
                        juros_dia='0.4% ao dia ',
                        acumulado=f'{duration * 0.4}% de juros acumulado'
                    )
                )

            elif duration > 5:
                delay_time.update(
                    dict(
                        atraso='Atraso acima de 5 dias ',
                        multa='7%',
                        juros_dia='0.6% ao dia ',
                        acumulado=f'{duration * 0.6}% de juros acumulado'
                    )
                )

            values_result = dict(
                id=i['id'],
                title=i['title'],
                date_loan=i['date_loan'],
                date_devolution=i['date_devolution'],
                is_reserve=i['is_reserve'],
                delay=delay_time

            )

            result.append(values_result)

        return Response(result, status.HTTP_200_OK)


class PostClientsViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Clients.objects.all()
    serializer_class = PostClientsSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.StaticHTMLRenderer, renderers.TemplateHTMLRenderer,)
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser,)
