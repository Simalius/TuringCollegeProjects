class MenuView:
    @staticmethod
    def display_menu():
        print("\nMain Menu")
        print("1. Add Recipe")
        print("2. View Stored Recipes")
        print("3. Create Shopping List")
        print("4. View Shopping Lists")
        print("5. Get Recipe Suggestion")
        print("6. Remove Recipe")
        print("7. Remove Shopping List")
        print("8. Exit")

    @staticmethod
    def get_user_choice():
        return input("Choose an option: ").strip()
