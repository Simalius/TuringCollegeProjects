def display_menu():
    print("\n--- Recipe Generator ---")
    print("1. Create a meal")
    print("2. View shopping list")
    print("3. Save shopping list to file")
    print("4. Exit")

def display_meals(meals):
    print("\nMeal Options:")
    for i, meal in enumerate(meals):
        print(f"{i + 1}. {meal.name}")

def display_recipes(recipes):
    print("\nAvailable Recipes:")
    for i, recipe in enumerate(recipes):
        print(f"{i + 1}. {recipe.name}")

def display_selected_meal(recipe):
    print("\nSelected Recipe:")
    print(recipe)
