from controllers.recipe_controller import RecipeController
from controllers.shopping_list_controller import ShoppingListController
from controllers.recipe_suggestion_controller import RecipeSuggestionController
from views.menu_view import MenuView

class MainController:
    def __init__(self):
        self.recipe_controller = RecipeController()
        self.shopping_list_controller = ShoppingListController()
        self.recipe_suggestion_controller = RecipeSuggestionController()

    def run(self):
        while True:
            MenuView.display_menu()
            choice = MenuView.get_user_choice()

            if choice == '1':
                self.recipe_controller.add_recipe()
            elif choice == '2':
                self.recipe_controller.view_recipes()
            elif choice == '3':
                self.shopping_list_controller.create_shopping_list(self.recipe_controller.recipes)
            elif choice == '4':
                self.shopping_list_controller.view_shopping_lists()
            elif choice == '5':
                self.recipe_suggestion_controller.handle_suggestion()  # Handles recipe suggestions
            elif choice == '6':
                self.recipe_controller.remove_recipe()
            elif choice == '7':
                self.shopping_list_controller.remove_shopping_list()
            elif choice == '8':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
