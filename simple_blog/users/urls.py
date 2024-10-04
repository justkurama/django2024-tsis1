from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile/<int:pk>/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<int:pk>/follow/', views.follow_user, name='follow_user'),
    path('profile/<int:pk>/unfollow/', views.unfollow_user, name='unfollow_user'),
]