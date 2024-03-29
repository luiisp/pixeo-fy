
from django.contrib import admin
from django.urls import path,include
from usrpixeo.api import viewsets as viewsets
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


routes = routers.DefaultRouter()

routes.register(r'images', viewsets.ImagesViewSet,basename="Images")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(routes.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
