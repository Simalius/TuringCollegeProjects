import os
from utils.file_manager import FileManager

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    @classmethod
    def load_recipes(cls, filename='data/recipes.json'):
        data = FileManager.read_json(filename)
        return [cls(name, details['ingredients']) for name, details in data.items()]

    @staticmethod
    def save_recipes(recipes, filename='data/recipes.json'):
        data = {recipe.name: {'ingredients': recipe.ingredients} for recipe in recipes}
        FileManager.write_json(data, filename)

    @staticmethod
    def add_recipe(recipe, filename='data/recipes.json'):
        recipes = Recipe.load_recipes(filename)
        if recipe.name in [r.name for r in recipes]:
            print(f"Recipe '{recipe.name}' already exists.")
        else:
            recipes.append(recipe)
            Recipe.save_recipes(recipes, filename)
            print(f"Recipe '{recipe.name}' added successfully.")
