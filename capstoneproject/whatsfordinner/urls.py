from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('available_vegetables/', views.available_vegetables, name="available_vegetables"),
    path('available_seasonings/', views.available_seasonings, name="available_seasonings"),
    path('available_oils/', views.available_oils, name="available_oils"),
    path('find_recipes/', views.find_recipes, name="find_recipes"),
    path('recipe/<int:recipe_id>/', views.recipe, name="recipe")
]
