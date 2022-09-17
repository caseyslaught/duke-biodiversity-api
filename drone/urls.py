from django.urls import path

from drone import views

urlpatterns = [

    path('create_flight/', views.CreateFlightView.as_view()),
    path('create_observation/', views.CreateObservationView.as_view()),
    path('get_flights/', views.GetFlightsView.as_view()),
    path('get_observations/', views.GetObservationsView.as_view())
    
]