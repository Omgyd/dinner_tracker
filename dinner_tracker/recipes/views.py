from django.shortcuts import render
from django.views.generic import CreateView
from .forms import RecipeForm
from .models import Recipe

# Create your views here.


def home(request):
    context = {"name": "Dinner Tracker"}
    return render(request, "recipes/home.html", context)


class CreateRecipeView(CreateView):
    model = Recipe
    template_name = "recipes/recipe_create.html"
    form_class = RecipeForm
