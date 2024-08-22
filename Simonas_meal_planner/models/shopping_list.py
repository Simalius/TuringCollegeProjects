from utils.file_manager import FileManager

class ShoppingList:
    def __init__(self, name, items=None):
        self.name = name
        self.items = items or {}

    def add_recipe(self, recipe):
        for ingredient, details in recipe.ingredients.items():
            if ingredient in self.items:
                self.items[ingredient]['amount'] += details['amount']
            else:
                self.items[ingredient] = details

    @classmethod
    def load_shopping_lists(cls, filename='data/shopping_lists.json'):
        data = FileManager.read_json(filename)
        return [cls(name, items) for name, items in data.items()]

    @staticmethod
    def save_shopping_lists(shopping_lists, filename='data/shopping_lists.json'):
        data = {shopping_list.name: shopping_list.items for shopping_list in shopping_lists}
        FileManager.write_json(data, filename)

    @staticmethod
    def add_shopping_list(shopping_list, filename='data/shopping_lists.json'):
        shopping_lists = ShoppingList.load_shopping_lists(filename)
        shopping_lists.append(shopping_list)
        ShoppingList.save_shopping_lists(shopping_lists, filename)
