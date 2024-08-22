class ShoppingListView:
    @staticmethod
    def display_shopping_lists(shopping_lists):
        if not shopping_lists:
            print("No shopping lists available.")
            return
        for i, shopping_list in enumerate(shopping_lists, 1):
            print(f"{i}. {shopping_list.name}")

    @staticmethod
    def display_shopping_list(shopping_list):
        print(f"\nShopping List: {shopping_list.name}")
        for item, details in shopping_list.items.items():
            print(f" - {item}: {details['amount']} {details['unit']}")

    @staticmethod
    def get_list_name():
        return input("Enter a name for the new shopping list: ").strip()

    @staticmethod
    def get_shopping_list_selection(shopping_lists):
        ShoppingListView.display_shopping_lists(shopping_lists)
        if not shopping_lists:
            return None
        try:
            selection = int(input("Enter the number of the shopping list to select: ")) - 1
            if 0 <= selection < len(shopping_lists):
                return selection
            else:
                print("Invalid selection.")
                return None
        except ValueError:
            print("Invalid input.")
            return None

    @staticmethod
    def prompt_save_to_file():
        return input("Would you like to save the shopping list to a file? (y/n): ").lower() == 'y'

    @staticmethod
    def prompt_send_via_email():
        return input("Would you like to send the shopping list via email? (y/n): ").lower() == 'y'

    @staticmethod
    def get_email():
        return input("Enter the recipient's email address: ").strip()
