
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Duke Biodiversity API",
      default_version='v1',
      description="API for processing observations from Duke Ocean/Rainforest Engineering projects.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="casey.slaught@duke.edu"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    # path('camera_trap/', include('camera_trap.urls')),
    path('drone/', include('drone.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('web/', include('web.urls')),

   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
