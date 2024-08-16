from create_meals import create_all_meals
from display import display_menu, display_meals, display_selected_meal, display_recipes
from shopping_list import ShoppingList

class MealPlanner:
    def __init__(self):
        self.shopping_list = ShoppingList()
        self.meals = create_all_meals()

    def handle_create_meal(self):
        print("\nCreating meals...")

        display_meals(self.meals)

        meal_choice = int(input("Select a meal type: ")) - 1

        if meal_choice not in range(len(self.meals)):
            print("Invalid choice. Please select a valid meal number.")
            return

        selected_meal = self.meals[meal_choice]

        display_recipes(selected_meal.recipes)
        recipe_choice = int(input(f"Select a recipe for {selected_meal.name} by entering the number: ")) - 1

        if recipe_choice not in range(len(selected_meal.recipes)):
            print("Invalid choice. Please select a valid recipe number.")
            return

        selected_recipe = selected_meal.recipes[recipe_choice]

        display_selected_meal(selected_recipe)

        self.shopping_list.add_recipe(selected_recipe)

        print("\nNew ingredients added to the shopping list:")
        self.shopping_list.display()

    def handle_view_shopping_list(self):
        self.shopping_list.display()

    def handle_save_shopping_list(self):
        self.shopping_list.save_to_file()

    def run(self):
        while True:
            display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.handle_create_meal()
            elif choice == '2':
                self.handle_view_shopping_list()
            elif choice == '3':
                self.handle_save_shopping_list()
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    planner = MealPlanner()
    planner.run()
