from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('available_vegetables/', views.available_vegetables, name="available_vegetables"),
    path('available_seasonings/', views.available_seasonings, name="available_seasonings"),
    path('select_vegetables/', views.select_vegetables, name="select_vegetables"),
]
