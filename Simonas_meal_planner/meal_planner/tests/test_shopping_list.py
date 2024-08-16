import pytest
from ingredients import Ingredient
from recipe import Recipe
from shopping_list import ShoppingList

def test_add_recipe():
    shopping_list = ShoppingList()
    ingredient = Ingredient("Tomato", 100, "grams", 2.0)
    recipe = Recipe("Tomato Soup")

    recipe.add_ingredient(ingredient)

    shopping_list.add_recipe(recipe)

    assert "Tomato" in shopping_list.items
    assert shopping_list.items["Tomato"]["quantity"] == 100
    assert shopping_list.items["Tomato"]["unit"] == "grams"
