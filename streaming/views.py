from django.shortcuts import render
from . import tests as t


stream_path = "http://localhost:8000/media/female.m3u8"


def home(request):
    # get thumbnails here
    # t.announce()
    return render(request, 'streaming/index.html', {'stream_path': stream_path})
''''
response = HttpResponse(f.read(), content_type=content_type)
            response['Content-Disposition'] = 'attachment; filename=%s' % filename
            response["Access-Control-Allow-Origin"] = '*'
            response["Access-Control-Allow-Methods"] = ['GET','PUT','OPTIONS']
            response["Access-Control-Max-Age"] = '1000'
            response["Access-Control-Allow-Headers"] = ['X-Requested-With', 'Content-Type']
            return response
'''
