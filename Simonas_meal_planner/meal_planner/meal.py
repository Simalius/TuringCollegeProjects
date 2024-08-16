class Meal:
    def __init__(self, name):
        self.name = name
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def total_calories(self):
        return sum(recipe.calculate_calories() for recipe in self.recipes)

    def __str__(self):
        recipes_str = "\n".join([str(recipe) for recipe in self.recipes])
        return f"Meal: {self.name}\n{recipes_str}\nTotal Calories: {self.total_calories()}"
