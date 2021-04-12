from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('available_vegetables/', views.available_vegetables, name="available_vegetables"),
    path('available_seasonings/', views.available_seasonings, name="available_seasonings"),
    # path('get_recipes/', views.get_recipes, name="get_recipes"),
    path('find_recipes/', views.find_recipes, name="find_recipes"),
]
