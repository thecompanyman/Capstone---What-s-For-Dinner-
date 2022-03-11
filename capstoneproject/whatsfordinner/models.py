from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    steps = models.TextField(null=True)
    source = models.TextField(null=True)
    recipe_ingredients = models.TextField(null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Ingredients(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RecipeIngredients(models.Model):
    recipe_name = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.ingredient

class Vegetables(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Seasonings(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name
    
class Oils(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name