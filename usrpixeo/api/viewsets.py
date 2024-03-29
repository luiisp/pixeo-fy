from rest_framework import viewsets
from usrpixeo.api import serializers
from usrpixeo import models

class ImagesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ImagesSerializer
    queryset = models.Images.objects.all()