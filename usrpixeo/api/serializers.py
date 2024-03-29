import rest_framework.serializers as serializers
from usrpixeo import models

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Images
        fields = '__all__'