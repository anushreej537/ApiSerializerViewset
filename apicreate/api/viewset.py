from .serializer import Registerserializer
from rest_framework import viewsets
from .models import *

class Registerviewset(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = Registerserializer

    