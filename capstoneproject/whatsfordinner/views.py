import json
from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Oils, Recipe, RecipeIngredients, Seasonings, Vegetables

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

def select_vegetables(request):
    # print(request.body)
    # data = json.loads(request.body)
    # print(data)
    # name = Vegetables.objects.values('name')
    # vegetable = Vegetables()
    # vegetable.name = name
    # vegetable.save()
    # print(vegetable.name)

    return JsonResponse({'message': 'ok'})
# def index(request):
#     veggies = Vegetables.objects.all()
#     seasonings = Seasonings.objects.all()
#     oils = Oils.objects.all()
#     recipes = Recipe.objects.all()[:10]
#     # ingredients = RecipeIngredients.objects.all()
#     context = {
#         'veggies': veggies,
#         'seasonings': seasonings,
#         'oils': oils,
#         'recipes': recipes,
#         # 'ingredients': ingredients,
#     }
#     return render(request, 'dinner/index.html', context)

# # def get_recipe(request):

# # use the request.POST to get the selections from the index file and then
# # .filter to search recipes that are saved -- recipe.objects.filter (specify filter in here -- match ingredients that are in recipe to ingredients that user selects)

# def get_recipe(request):
#     recipe = Recipe()
#     recipe.save()

#     return HttpResponseRedirect(reverse('index'))

# def find_recipes(request):
#     form = request.POST
#     selected_veggies = form['selectedveggies']
#     veggies = Vegetables.objects.get(name=selected_veggies)
#     veggie = Vegetables()
#     veggie.name = veggies
#     veggie.save()

#     return HttpResponseRedirect(reverse('index'))