from simpleapi.models import Port, Boat
from rest_framework import viewsets
from simpleapi.serializers import PortSerializer, BoatSerializer


class PortViewSet(viewsets.ModelViewSet):
    queryset = Port.objects.all()
    serializer_class = PortSerializer


class BoatViewSet(viewsets.ModelViewSet):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer

