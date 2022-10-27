from django.urls import path

from drone import views

urlpatterns = [

    path('create_flight/', views.CreateDroneFlightView.as_view()),
    path('create_media/', views.CreateDroneMediaView.as_view()),
    path('get_flights/', views.GetDroneFlightsView.as_view()),
    
]