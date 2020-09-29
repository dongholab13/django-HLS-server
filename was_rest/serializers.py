from rest_framework import serializers
from .models import *

class Stream_1Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stream_1
        fields = ('pk', 'name', 'file_list')

class Stream_2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stream_2
        fields = ('pk', 'name', 'file_list')

class Stream_3Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stream_3
        fields = ('pk', 'name', 'file_list')

