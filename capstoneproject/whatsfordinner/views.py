import json
from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Oils, Recipe, Ingredients, RecipeIngredients, Seasonings, Vegetables

# Create your views here.


def index(request):
    return render(request, 'whatsfordinner/index.html')


def available_vegetables(request):
    user_vegetables = Vegetables.objects.order_by('name').values('name')
    output = list(user_vegetables)
    # print(output)

    return JsonResponse(output, safe=False)

def available_seasonings(request):
    user_seasonings = Seasonings.objects.values('name')
    output = list(user_seasonings)
    # print(output)

    return JsonResponse(output, safe=False)

def find_recipes(request):
    data = json.loads(request.body)
    # print(data)
    ingredient_list = ''
    for i in data["submittedIngredients"]:
        ingredient_list += f"(.*{i}.*)"
    print(ingredient_list)
    # regex = " + ".join(ingredient_list)
    # print(regex)
    recipes = Recipe.objects.filter(recipe_ingredients__iregex=ingredient_list)
    recipeingredientoutput = []
    output = []
    # recipe_list = []
    for recipe in recipes:
        for ingredient in recipe.recipeingredients_set.values('ingredient'):
            recipeingredientoutput.append(ingredient)
        # for item in recipeingredientoutput:
        #     for key in item:
        #         recipe_list.append(item[key])
        output.append({
            'name': recipe.name,
            'ingredients': recipeingredientoutput,
            'recipe_list': recipe.recipe_ingredients,
            'steps': recipe.steps,
            'source': recipe.source
        })
        recipeingredientoutput = []
    # print(output)
    # print(recipe_list)
    # print(recipeingredientoutput)
    return JsonResponse(output, safe=False)