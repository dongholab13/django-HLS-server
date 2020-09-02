from django.shortcuts import render
from django.http import HttpResponse, Http404
import os
import mimetypes

# Create your views here.
def stream(request, filename):
    print("stream")
    filepath = os.path.join('media/file/',filename)
    content_type = mimetypes.guess_type(filepath)[0]
    print(mimetypes.guess_type(filepath)[0])
    print(os.path.exists(filepath))
    if os.path.exists(filepath):
        with open(filepath) as f:
            response = HttpResponse(f.read(), content_type=content_type)
            response['Content-Disposition'] = 'attachment; filename=%s' % filename
            response["Access-Control-Allow-Origin"] = '*'
            response["Access-Control-Allow-Methods"] = ['GET','PUT','OPTIONS']
            response["Access-Control-Max-Age"] = '1000'
            response["Access-Control-Allow-Headers"] = ['X-Requested-With', 'Content-Type']
            return response
    raise Http404

