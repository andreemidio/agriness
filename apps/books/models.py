import uuid

from django.db import models

# Create your models here.
from apps.clients.models import Clients


class Books(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    date_loan = models.DateField(null=True, blank=True)
    date_devolution = models.DateField(null=True, blank=True)
    is_reserve = models.BooleanField(default=False)
    client_reserve = models.ForeignKey(Clients, on_delete=models.DO_NOTHING, null=True, blank=True)
