from datetime import datetime

class ShoppingList:
    def __init__(self):
        self.items = {}

    def add_recipe(self, recipe):
        for ingredient in recipe.ingredients:
            if ingredient.name in self.items:
                self.items[ingredient.name]['quantity'] += ingredient.quantity
            else:
                self.items[ingredient.name] = {
                    'quantity': ingredient.quantity,
                    'unit': ingredient.unit
                }

    def display(self):
        if not self.items:
            print("\nShopping list is empty.")
        else:
            print("\nShopping List:")
            for item, details in self.items.items():
                print(f"{details['quantity']} {details['unit']} of {item}")

    def save_to_file(self):
        if not self.items:
            print("\nShopping list is empty. Nothing to save.")
            return

        date_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"shopping_list_{date_stamp}.txt"

        file_content = "Shopping List\n"
        file_content += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        for item, details in self.items.items():
            file_content += f"{details['quantity']} {details['unit']} of {item}\n"

        with open(filename, 'w') as file:
            file.write(file_content)

        print(f"\nShopping list saved successfully as {filename}.")
