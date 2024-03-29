from rest_framework import viewsets
from usrpixeo.api import serializers
from rest_framework.permissions import IsAuthenticated
from usrpixeo import models

class ImagesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ImagesSerializer
    queryset = models.Images.objects.all()