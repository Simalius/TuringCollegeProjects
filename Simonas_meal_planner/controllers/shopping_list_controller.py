from models.shopping_list import ShoppingList
from views.shopping_list_view import ShoppingListView
from controllers.email_controller import EmailController
from utils.file_converter import FileConverter

class ShoppingListController:
    def __init__(self):
        self.shopping_lists = ShoppingList.load_shopping_lists()
        self.email_controller = EmailController()

    def create_shopping_list(self, recipes):
        if not recipes:
            print("No recipes available. Please add some recipes first.")
            return

        index = ShoppingListView.get_shopping_list_selection(recipes)
        if index is None:
            return

        selected_recipe = recipes[index]
        list_name = ShoppingListView.get_list_name()
        if not list_name:
            print("Shopping list name cannot be empty.")
            return

        new_shopping_list = ShoppingList(list_name)
        new_shopping_list.add_recipe(selected_recipe)
        ShoppingList.add_shopping_list(new_shopping_list)
        self.shopping_lists.append(new_shopping_list)
        print(f"Shopping list '{list_name}' created successfully.")

    def view_shopping_lists(self):
        index = ShoppingListView.get_shopping_list_selection(self.shopping_lists)
        if index is not None:
            ShoppingListView.display_shopping_list(self.shopping_lists[index])
            
            if ShoppingListView.prompt_save_to_file():
                file_path = FileConverter.shopping_list_to_text(self.shopping_lists[index], 'shopping_list.txt')
                print(f"Shopping list saved to {file_path}.")
            
            if ShoppingListView.prompt_send_via_email():
                email = ShoppingListView.get_email()
                subject = f"Shopping List: {self.shopping_lists[index].name}"
                body = f"Here is your shopping list: {self.shopping_lists[index].name}"
                file_path = FileConverter.shopping_list_to_text(self.shopping_lists[index], 'shopping_list.txt')
                self.email_controller.send_shopping_list(email, subject, body, file_path)
        else:
            print("No shopping list selected.")

    def remove_shopping_list(self):
        index = ShoppingListView.get_shopping_list_selection(self.shopping_lists)
        if index is not None:
            removed_list = self.shopping_lists.pop(index)
            ShoppingList.save_shopping_lists(self.shopping_lists)
            print(f"Shopping list '{removed_list.name}' removed successfully.")
