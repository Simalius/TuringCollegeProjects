import pytest
from ingredients import Ingredient
from recipe import Recipe
from meal import Meal

def test_meal_initialization():
    meal = Meal("Dinner")
    assert meal.name == "Dinner"
    assert meal.recipes == []

def test_add_recipe():
    meal = Meal("Dinner")
    recipe = Recipe("Tomato Soup")
    meal.add_recipe(recipe)
    assert len(meal.recipes) == 1
    assert meal.recipes[0] == recipe

def test_total_calories():
    meal = Meal("Dinner")
    ingredient1 = Ingredient("Tomato", 100, "grams", 2.0)
    ingredient2 = Ingredient("Onion", 50, "grams", 1.5)
    recipe1 = Recipe("Tomato Soup")
    recipe1.add_ingredient(ingredient1)
    recipe1.add_ingredient(ingredient2)
    meal.add_recipe(recipe1)
    assert meal.total_calories() == 200.0 + 75.0

def test_str_method():
    meal = Meal("Dinner")
    ingredient = Ingredient("Tomato", 100, "grams", 2.0)
    recipe = Recipe("Tomato Soup")
    recipe.add_ingredient(ingredient)
    meal.add_recipe(recipe)
    assert str(meal) == ("Meal: Dinner\n"
                         "Recipe: Tomato Soup\nIngredients:\n"
                         "100 grams of Tomato (200.0 calories)\n"
                         "Total Calories: 200.0")
