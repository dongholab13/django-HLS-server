from rest_framework import serializers, viewsets, status, generics, filters
from rest_framework.response import Response
from .models import *
from .serializers import *
import json
from ipc_server import settings
import os
from rest_framework.decorators import action

'''
class StreamTrajectoryViewset(viewsets.ModelViewSet):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer

    def create(self, request, *args, **kwargs):
        if request.method =="POST":
            # print(self.request.data['ts_file_loc'])
            #json_request = json.loads(self.request.body.decode('utf-8'))
            ts_file_loc = self.request.data['ts_file_loc']
            print(ts_file_loc)
            ts_file_name = ts_file_loc.split('/')[-1]
            f = open( os.path.join(os.path.join(settings.MEDIA_ROOT, 'stream_trajectory'), 'male.m3u8') , 'a')
            ##EXTINF:16.666667,
            #http://192.168.0.43:9031/file/female0.ts
            f.write("#EXTINF:1.0\n")
            f.write("http://192.168.0.43:9031/stream_trajectory/" + ts_file_name + '\n')
            f.close()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

class Stream_1Viewset(viewsets.ModelViewSet):
    queryset = Stream_1.objects.all()
    serializer_class = Stream_1Serializer

    @action(methods=['POST'],detail=False)
    def singleImage(self, requests, *args, **kwargs):
        file_path = self.request.data['file_path']
        target_stream = Stream_1.objects.get(pk=1)
        target_stream.file_list = str(target_stream.file_list) + file_path + ","
        target_stream.save()
        print(file_path)
        return Response("testststs")

    @action(methods=['GET'],detail=False)
    def getImage(self, requests, *args, **kwargs):
        target_stream = Stream_1.objects.get(pk=1)
        file_path = target_stream.file_list.split(',')[0]
        target_stream.file_list = target_stream.file_list.replace(file_path + ',','')
        target_stream.save()
        if file_path == '':
            return Response('no_file')
        return Response(file_path)

class Stream_2Viewset(viewsets.ModelViewSet):
    queryset = Stream_2.objects.all()
    serializer_class = Stream_2Serializer

    @action(methods=['POST'],detail=False)
    def singleImage(self, requests, *args, **kwargs):
        file_path = self.request.data['file_path']
        target_stream = Stream_2.objects.get(pk=1)
        target_stream.file_list = str(target_stream.file_list) + file_path + ","
        target_stream.save()
        print(file_path)
        return Response("testststs")

    @action(methods=['GET'],detail=False)
    def getImage(self, requests, *args, **kwargs):
        target_stream = Stream_2.objects.get(pk=1)
        file_path = target_stream.file_list.split(',')[0]
        target_stream.file_list = target_stream.file_list.replace(file_path + ',','')
        target_stream.save()
        if file_path == '':
            return Response('no_file')
        return Response(file_path)


class Stream_3Viewset(viewsets.ModelViewSet):
    queryset = Stream_3.objects.all()
    serializer_class = Stream_3Serializer

    @action(methods=['POST'],detail=False)
    def singleImage(self, requests, *args, **kwargs):
        file_path = self.request.data['file_path']
        target_stream = Stream_3.objects.get(pk=1)
        target_stream.file_list = str(target_stream.file_list) + file_path + ","
        target_stream.save()
        print(file_path)
        return Response("testststs")

    @action(methods=['GET'],detail=False)
    def getImage(self, requests, *args, **kwargs):
        target_stream = Stream_3.objects.get(pk=1)
        file_path = target_stream.file_list.split(',')[0]
        target_stream.file_list = target_stream.file_list.replace(file_path + ',','')
        target_stream.save()
        if file_path == '':
            return Response('no_file')
        return Response(file_path)