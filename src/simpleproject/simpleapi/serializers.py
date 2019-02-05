from simpleapi.models import Port, Boat
from rest_framework import serializers


class PortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Port
        fields = ('name', 'rating')


class BoatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boat
        fields = ('name', 'cabins', 'port')

