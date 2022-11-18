from django.urls import path

from drone import views

urlpatterns = [
    path('create_drone/', views.CreateDroneVehicleView.as_view()),
    path('create_flight/', views.CreateDroneFlightView.as_view()),
    path('create_media/', views.CreateDroneMediaView.as_view()),
    path('get_drones/', views.GetDroneVehiclesView.as_view()),
    path('get_flights/', views.GetDroneFlightsView.as_view()),
    path('get_media/', views.GetDroneMediaView.as_view()),
    path('get_observations/', views.GetDroneObservationsView.as_view()),
    # TODO: put drone
    
]