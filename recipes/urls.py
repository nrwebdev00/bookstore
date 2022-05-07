from django.urls import path

from . import views

urlpatterns = [
    path('', views.recipes, name='recipes-recipes'),
    path('single/<str:pk>/', views.recipe, name='recipes-single'),
    path('list/<str:tag>/<int:page>', views.recipesList, name='recipes-list'),
    path('search/<str:q>/<int:page>', views.recipesListString, name='recipes-search'),
]