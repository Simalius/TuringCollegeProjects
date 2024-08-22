from utils.spoonacular_client import SpoonacularClient
from models.recipe import Recipe
from views.recipe_suggestion_view import RecipeSuggestionView

class RecipeSuggestionController:
    def __init__(self):
        self.api_client = SpoonacularClient()

    def handle_suggestion(self):
        suggestion = self.api_client.get_random_recipe()
        if suggestion:
            RecipeSuggestionView.display_suggestion(suggestion)
            if RecipeSuggestionView.ask_to_add_recipe():
                name = suggestion['name']
                ingredients = suggestion['ingredients']
                new_recipe = Recipe(name, ingredients)
                Recipe.add_recipe(new_recipe)
                print(f"Recipe '{name}' added successfully.")
        else:
            print("No recipe suggestion was retrieved.")
