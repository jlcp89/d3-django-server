from rest_framework import viewsets
from .serializer import MailSerializer
from .models import Mail

# Create your views here.

class MailView(viewsets.ModelViewSet):
    serializer_class = MailSerializer
    queryset = Mail.objects.all()

