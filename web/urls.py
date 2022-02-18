from django.urls import path

from web import views

urlpatterns = [

    path('get_observations/', views.GetObservationsView.as_view())
    
]