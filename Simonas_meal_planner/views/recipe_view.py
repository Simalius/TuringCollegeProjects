class RecipeView:
    @staticmethod
    def display_recipes(recipes):
        if not recipes:
            print("No recipes available.")
            return
        for i, recipe in enumerate(recipes, 1):
            print(f"{i}. {recipe.name}")

    @staticmethod
    def display_recipe(recipe):
        print(f"\nRecipe: {recipe.name}")
        for ingredient, details in recipe.ingredients.items():
            print(f" - {ingredient}: {details['amount']} {details['unit']}")

    @staticmethod
    def get_recipe_details():
        name = input("Enter recipe name: ").strip()
        ingredients = {}
        while True:
            ingredient_name = input("Enter ingredient name (or type 'done' to finish): ").strip()
            if ingredient_name.lower() == 'done':
                break
            amount = float(input(f"Enter amount for {ingredient_name}: "))
            unit = input(f"Enter unit for {ingredient_name}: ")
            ingredients[ingredient_name] = {'amount': amount, 'unit': unit}
        return name, ingredients

    @staticmethod
    def get_recipe_selection(recipes):
        RecipeView.display_recipes(recipes)
        if not recipes:
            return None
        try:
            selection = int(input("Enter the number of the recipe to select: ")) - 1
            if 0 <= selection < len(recipes):
                return selection
            else:
                print("Invalid selection.")
                return None
        except ValueError:
            print("Invalid input.")
            return None
