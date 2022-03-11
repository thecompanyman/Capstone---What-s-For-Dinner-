import json
from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Oils, Recipe, Ingredients, RecipeIngredients, Seasonings, Vegetables


def index(request):
    return render(request, 'whatsfordinner/index.html')

def available_vegetables(request):
    # Outputs a list of selected vegetables by user
    user_vegetables = Vegetables.objects.order_by('name').values('name')
    output = list(user_vegetables)

    return JsonResponse(output, safe=False)

def available_seasonings(request):
    # Outputs a list of selected seasonings by user
    user_seasonings = Seasonings.objects.values('name')
    output = list(user_seasonings)

    return JsonResponse(output, safe=False)

def available_oils(request):
    # Outputs a list of selected oils by user
    user_oils = Oils.objects.values('name')
    output = list(user_oils)

    return JsonResponse(output, safe=False)

def find_recipes(request):
    # Finds matching recipes based on ingredient selection
    data = json.loads(request.body)
    ingredient_list = ''
    for i in data["submittedIngredients"]:
        ingredient_list += f"(.*{i}.*)"
    print(ingredient_list)

    recipes = Recipe.objects.filter(recipe_ingredients__iregex=ingredient_list)
    recipeingredientoutput = []
    output = []
    for recipe in recipes:
        for ingredient in recipe.recipeingredients_set.values('ingredient'):
            recipeingredientoutput.append(ingredient)
        output.append({
            'name': recipe.name,
            'ingredients': recipeingredientoutput,
            'recipe_list': recipe.recipe_ingredients,
            'steps': recipe.steps,
            'source': recipe.source,
            'id': recipe.id
        })
        recipeingredientoutput = []

    return JsonResponse(output, safe=False)

def recipe(request, recipe_id):
    # Outputs matching recipe names, steps, and ingredients
    recipes = get_object_or_404(Recipe, id=recipe_id)
    recipeingredientoutput = []
    for ingredient in recipes.recipeingredients_set.values('ingredient'):
            recipeingredientoutput.append(ingredient)
    context = {
        'recipes': recipes,
        'ingredients': recipeingredientoutput,
    }
    print(recipeingredientoutput)
    
    return render(request, 'whatsfordinner/recipe.html', context)