from django.urls import path

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("recipes/", views.CreateRecipeView.as_view(), name="create_recipe"),
    ]