import requests
import os

class SpoonacularClient:
    def __init__(self):
        self.api_key = os.getenv("SPOONACULAR_API_KEY")
        self.base_url = "https://api.spoonacular.com/recipes"

    def get_random_recipe(self):
        if not self.api_key:
            print("API key for Spoonacular is not set. Please check your .env file.")
            return None
        
        url = f"{self.base_url}/random"
        params = {"apiKey": self.api_key, "number": 1}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            recipe_data = response.json()
            recipe = recipe_data['recipes'][0]
            name = recipe['title']
            ingredients = {
                item['name']: {'amount': item['amount'], 'unit': item['unit']}
                for item in recipe['extendedIngredients']
            }
            return {'name': name, 'ingredients': ingredients}
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch recipe: {e}")
            return None
