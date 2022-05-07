from django.urls import path

from . import views

urlpatterns = [
    path('', views.users, name='users-users'),
    path('profile/', views.profile, name='users-profile'),
    path('favorite-remove/<str:pk>/', views.delFavorite, name='favorite-del'),
    path('favorite-add/<int:id>/', views.addFavorite, name='favorite-add'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]