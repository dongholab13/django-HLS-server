from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from .viewsets import *

router = routers.DefaultRouter()
#router.register(r'mediafiles', MediaFileViewset)
#router.register(r'stream-trajectory', StreamTrajectoryViewset)
#router.register(r'heatmap', HeatmapViewset)
router.register(r'stream1', Stream_1Viewset)
router.register(r'stream2', Stream_2Viewset)
router.register(r'stream3', Stream_3Viewset)

app_name = 'api'
urlpatterns = [
    url(r'^', include(router.urls), ),
    url(r'^api-auth/', include('rest_framework.urls', namespace='api')),
]