
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('drone/', include('drone.urls')),
    path('jet/', include('jet.urls', 'jet')),
]
