from django.urls import include, path

from drone import views

urlpatterns = [

    path('add_observation/', views.AddObservationView.as_view()),
    path('get_observations/', views.GetObservationsView.as_view())
    
]