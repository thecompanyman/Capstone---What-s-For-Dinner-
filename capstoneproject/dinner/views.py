from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Recipe, Vegetables, Seasonings, Oils, RecipeIngredients

# Create your views here.

def index(request):
    veggies = Vegetables.objects.all()
    seasonings = Seasonings.objects.all()
    oils = Oils.objects.all()
    recipes = Recipe.objects.all()[:10]
    # ingredients = RecipeIngredients.objects.all()
    context = {
        'veggies': veggies,
        'seasonings': seasonings,
        'oils': oils,
        'recipes': recipes,
        # 'ingredients': ingredients,
    }
    return render(request, 'dinner/index.html', context)




# def get_recipe(request):

# use the request.POST to get the selections from the index file and then
# .filter to search recipes that are saved -- recipe.objects.filter (specify filter in here -- match ingredients that are in recipe to ingredients that user selects)

def get_recipe(request):
    recipe = Recipe()
    recipe.save()

    return HttpResponseRedirect(reverse('index'))