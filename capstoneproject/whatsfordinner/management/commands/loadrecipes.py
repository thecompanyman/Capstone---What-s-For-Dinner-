import json
from django.core.management.base import BaseCommand
from whatsfordinner.models import Recipe, RecipeIngredients

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        with open('recipes.json', 'r') as file:
            data = file.read()

        all_recipes = json.loads(data)
        Recipe.objects.all().delete()
        # RecipeIngredients.objects.all().delete()

        for recipes in all_recipes:
            recipe = Recipe()
            recipe.name = all_recipes[recipes]['name']
            recipe.steps = all_recipes[recipes]['instructions']
            recipe.source = all_recipes[recipes]['source']
            # print(recipe.name)
            # print(recipe.source)
            # print(recipe.steps)
            recipe.save()

            for i in all_recipes[recipes]['ingredients']:
                ingredients = RecipeIngredients()
                ingredients.recipe_name = recipe
                ingredients.ingredient = i
                ingredients.save()
                # print(ingredients)

