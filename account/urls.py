from django.urls import  path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from account import views


urlpatterns = [

    path('auth_test/', views.AuthTestView.as_view()),
    path('get_account/', views.GetAccountView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('test/', views.AuthTestView.as_view())

]