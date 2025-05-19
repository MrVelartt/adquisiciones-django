from django.urls import path, re_path
from .views import (
    AcquisitionListCreateAPIView,
    AcquisitionDetailAPIView,
    AcquisitionHistorialAPIView
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de Swagger/OpenAPI
schema_view = get_schema_view(
    openapi.Info(
        title="Adquisiciones API",
        default_version='v1',
        description="Documentación de la API de adquisiciones",
        contact=openapi.Contact(email="contacto@tuempresa.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Endpoints de tu API
    path(
        'acquisitions/',
        AcquisitionListCreateAPIView.as_view(),
        name='acquisition-list-create'
    ),
    path(
        'acquisitions/<int:pk>/',
        AcquisitionDetailAPIView.as_view(),
        name='acquisition-detail'
    ),
    path(
        'acquisitions/<int:pk>/historial/',
        AcquisitionHistorialAPIView.as_view(),
        name='acquisition-historial'
    ),

    # Documentación Swagger y ReDoc
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
