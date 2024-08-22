import pytest
from models.recipe import Recipe

def test_recipe_initialization():
    recipe = Recipe("Test Recipe", {"ingredient1": {"amount": 2, "unit": "cups"}})
    assert recipe.name == "Test Recipe"
    assert "ingredient1" in recipe.ingredients
