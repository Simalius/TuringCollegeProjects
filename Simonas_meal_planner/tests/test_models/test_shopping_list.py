import pytest
from models.shopping_list import ShoppingList
from models.recipe import Recipe

def test_shopping_list_initialization():
    shopping_list = ShoppingList("Test List")
    assert shopping_list.name == "Test List"
    assert shopping_list.items == {}

def test_add_recipe_to_shopping_list():
    shopping_list = ShoppingList("Test List")
    recipe = Recipe("Test Recipe", {"ingredient1": {"amount": 2, "unit": "cups"}})
    shopping_list.add_recipe(recipe)
    assert "ingredient1" in shopping_list.items
