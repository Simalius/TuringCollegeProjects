class RecipeSuggestionView:
    @staticmethod
    def display_suggestion(suggestion):
        print("\nRecipe Suggestion:")
        print(f"Name: {suggestion['name']}")
        print("Ingredients:")
        for ingredient, details in suggestion['ingredients'].items():
            print(f" - {ingredient}: {details['amount']} {details['unit']}")

    @staticmethod
    def ask_to_add_recipe():
        return input("Would you like to add this recipe to your collection? (y/n): ").strip().lower() == 'y'
