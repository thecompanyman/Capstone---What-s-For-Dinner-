from django.contrib import admin
from .models import Recipe, Vegetables, Ingredients, Seasonings, Oils, RecipeIngredients


class RecipeIngredientsInline(admin.TabularInline):
    model = RecipeIngredients

class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        RecipeIngredientsInline,
    ]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Vegetables)
admin.site.register(Seasonings)
admin.site.register(Oils)
admin.site.register(RecipeIngredients)
admin.site.register(Ingredients)
