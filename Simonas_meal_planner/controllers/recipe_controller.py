from models.recipe import Recipe
from views.recipe_view import RecipeView

class RecipeController:
    def __init__(self):
        self.recipes = Recipe.load_recipes()

    def add_recipe(self):
        name, ingredients = RecipeView.get_recipe_details()
        new_recipe = Recipe(name, ingredients)
        Recipe.add_recipe(new_recipe)
        self.recipes.append(new_recipe)

    def view_recipes(self):
        RecipeView.display_recipes(self.recipes)

    def remove_recipe(self):
        index = RecipeView.get_recipe_selection(self.recipes)
        if index is not None:
            removed_recipe = self.recipes.pop(index)
            Recipe.save_recipes(self.recipes)
            print(f"Recipe '{removed_recipe.name}' removed successfully.")
