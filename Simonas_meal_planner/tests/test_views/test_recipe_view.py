import pytest
from views.recipe_view import RecipeView
from models.recipe import Recipe

def test_display_recipes(capsys):
    recipes = [Recipe("Test Recipe", {"ingredient1": {"amount": 2, "unit": "cups"}})]
    RecipeView.display_recipes(recipes)
    captured = capsys.readouterr()
    assert "Test Recipe" in captured.out
