from django.urls import path

from drone import views

urlpatterns = [

    path('add_flight/', views.AddFlightView.as_view()),
    path('add_observation/', views.AddObservationView.as_view()),
    path('get_flights/', views.GetFlightsView.as_view()),
    path('get_observations/', views.GetObservationsView.as_view())
    
]