import pytest
from ingredients import Ingredient
from recipe import Recipe

def test_recipe_initialization():
    recipe = Recipe("Tomato Soup")
    assert recipe.name == "Tomato Soup"
    assert recipe.ingredients == []

def test_add_ingredient():
    recipe = Recipe("Tomato Soup")
    ingredient = Ingredient("Tomato", 100, "grams", 2.0)
    recipe.add_ingredient(ingredient)
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0] == ingredient

def test_calculate_calories():
    recipe = Recipe("Tomato Soup")
    ingredient1 = Ingredient("Tomato", 100, "grams", 2.0)
    ingredient2 = Ingredient("Onion", 50, "grams", 1.5)
    recipe.add_ingredient(ingredient1)
    recipe.add_ingredient(ingredient2)
    assert recipe.calculate_calories() == 200.0 + 75.0

def test_str_method():
    recipe = Recipe("Tomato Soup")
    ingredient = Ingredient("Tomato", 100, "grams", 2.0)
    recipe.add_ingredient(ingredient)
    assert str(recipe) == "Recipe: Tomato Soup\nIngredients:\n100 grams of Tomato (200.0 calories)"
