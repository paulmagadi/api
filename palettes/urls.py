from django.urls import path
from .views import PaletteListCreate, PaletteRetrieveUpdateDestroy

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Color Palette",
      default_version='v1',
      description="Color Palettes APIs. Allows POST, PUT, GET and DELETE requests",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="paulsqmagadi@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('palettes/', PaletteListCreate.as_view()),
    path('palettes/<int:pk>/', PaletteRetrieveUpdateDestroy.as_view()),  
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


