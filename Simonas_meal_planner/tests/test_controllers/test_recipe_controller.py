import pytest
from controllers.recipe_controller import RecipeController
from models.recipe import Recipe

def test_add_recipe(mocker):
    # Ensure the recipes list is empty before starting the test
    controller = RecipeController()
    controller.recipes = []

    # Mock the input method to return a predefined recipe
    mocker.patch('views.recipe_view.RecipeView.get_recipe_details', return_value=("Test Recipe", {"ingredient1": {"amount": 2, "unit": "cups"}}))
    
    # Run the method under test
    controller.add_recipe()
    
    # Check that the recipe was added
    assert len(controller.recipes) == 1
    assert controller.recipes[0].name == "Test Recipe"
