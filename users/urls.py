from django.urls import path 
from . import views

urlpatterns = [
    path('me/', views.CurrentUser.as_view()),
    path('update_profile/', views.UpdateProfile.as_view())
]