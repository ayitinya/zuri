from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer


class PersonAPI(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class PersonDetailAPI(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer