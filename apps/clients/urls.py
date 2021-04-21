from django.urls import path, include
from rest_framework import routers

from apps.clients.viewsets import ListClientsViewSet, PostClientsViewSet

app_name = 'clients'

router = routers.DefaultRouter()

router.register(r'clients', ListClientsViewSet, basename='client-tipology')
router.register(r'clients/add', PostClientsViewSet, basename='client-tipology')

urlpatterns = [
    path(r'', include(router.urls)),
]
