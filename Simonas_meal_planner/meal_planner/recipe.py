class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def calculate_calories(self):
        return sum(ingredient.total_calories() for ingredient in self.ingredients)

    def __str__(self):
        ingredients_str = "\n".join([str(ingredient) for ingredient in self.ingredients])
        return f"Recipe: {self.name}\nIngredients:\n{ingredients_str}"

