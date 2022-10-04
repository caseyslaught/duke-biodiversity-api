from django.urls import path

from drone import views

urlpatterns = [

    path('create_flight/', views.CreateDroneFlightView.as_view()),
    path('create_photo/', views.CreateDronePhotoView.as_view()),
    path('get_flights/', views.GetDroneFlightsView.as_view()),
    path('get_photos/', views.GetDronePhotosView.as_view())
    
]