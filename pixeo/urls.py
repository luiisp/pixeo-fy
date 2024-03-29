
from django.contrib import admin
from django.urls import path, include
from usrpixeo.api import viewsets as viewsets
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

routes = routers.DefaultRouter()

routes.register(r'images', viewsets.ImagesViewSet, basename="Images")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_schema', get_schema_view(title='Pixeo API', description='Pixeo Images Storage Api, Acess the repo: https://github.com/luiisp/pixeo-fy'), name='api-schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api-schema'}
        ), name='swagger-ui'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(routes.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
URL Configuration

This module defines the URL patterns for the Pixeo application. It includes the following:

- Admin URL: '/admin/' - Provides access to the Django admin interface.
- Token URL: '/token/' - Generates a JSON Web Token (JWT) for authentication.
- Token Refresh URL: '/token/refresh/' - Refreshes an existing JWT.
- API URLs: '/api/' - Includes the registered routes for the Pixeo API.
- Media URLs: '/media/' - Serves media files uploaded by users.

Note: This module assumes the presence of the following packages:
- django.contrib.admin
- django.urls
- usrpixeo.api.viewsets
- rest_framework.routers
- django.conf.settings
- django.conf.urls.static
- rest_framework_simplejwt.views.TokenObtainPairView
- rest_framework_simplejwt.views.TokenRefreshView
"""
