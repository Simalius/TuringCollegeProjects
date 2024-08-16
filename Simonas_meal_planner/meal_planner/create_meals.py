from ingredients import Ingredient
from recipe import Recipe
from meal import Meal

def create_ingredients():
    pasta = Ingredient("Pasta", 200, "grams", 1.5)
    tomato_sauce = Ingredient("Tomato Sauce", 100, "ml", 0.5)
    cheese = Ingredient("Cheese", 50, "grams", 4.0)
    bread = Ingredient("Bread", 2, "slices", 70)
    butter = Ingredient("Butter", 10, "grams", 7.2)
    grilled_chicken = Ingredient("Chicken Breast", 200, "grams", 2.5)
    olive_oil = Ingredient("Olive Oil", 15, "ml", 1.2)
    seasoning = Ingredient("Seasoning", 5, "grams", 0.5)
    eggs = Ingredient("Eggs", 2, "pieces", 150)
    milk = Ingredient("Milk", 200, "ml", 0.5)
    bacon = Ingredient("Bacon", 100, "grams", 5.0)

    return {
        "pasta": pasta,
        "tomato_sauce": tomato_sauce,
        "cheese": cheese,
        "bread": bread,
        "butter": butter,
        "grilled_chicken": grilled_chicken,
        "olive_oil": olive_oil,
        "seasoning": seasoning,
        "eggs": eggs,
        "milk": milk,
        "bacon": bacon
    }

def create_recipes(ingredients):
    scrambled_eggs = Recipe("Scrambled Eggs")
    scrambled_eggs.add_ingredient(ingredients["eggs"])
    scrambled_eggs.add_ingredient(ingredients["milk"])

    bacon_and_eggs = Recipe("Bacon and Eggs")
    bacon_and_eggs.add_ingredient(ingredients["bacon"])
    bacon_and_eggs.add_ingredient(ingredients["eggs"])

    pasta_recipe = Recipe("Pasta with Tomato Sauce")
    pasta_recipe.add_ingredient(ingredients["pasta"])
    pasta_recipe.add_ingredient(ingredients["tomato_sauce"])
    pasta_recipe.add_ingredient(ingredients["cheese"])

    grilled_chicken = Recipe("Grilled Chicken with Olive Oil")
    grilled_chicken.add_ingredient(ingredients["grilled_chicken"])
    grilled_chicken.add_ingredient(ingredients["olive_oil"])
    grilled_chicken.add_ingredient(ingredients["seasoning"])

    butter_toast = Recipe("Butter Toast")
    butter_toast.add_ingredient(ingredients["bread"])
    butter_toast.add_ingredient(ingredients["butter"])

    cheese_pasta = Recipe("Cheese Pasta")
    cheese_pasta.add_ingredient(ingredients["pasta"])
    cheese_pasta.add_ingredient(ingredients["cheese"])

    return {
        "scrambled_eggs": scrambled_eggs,
        "bacon_and_eggs": bacon_and_eggs,
        "pasta_recipe": pasta_recipe,
        "grilled_chicken": grilled_chicken,
        "butter_toast": butter_toast,
        "cheese_pasta": cheese_pasta
    }

def create_meals(recipes):
    breakfast = Meal("Breakfast")
    breakfast.add_recipe(recipes["scrambled_eggs"])
    breakfast.add_recipe(recipes["bacon_and_eggs"])

    lunch = Meal("Lunch")
    lunch.add_recipe(recipes["pasta_recipe"])
    lunch.add_recipe(recipes["grilled_chicken"])

    dinner = Meal("Dinner")
    dinner.add_recipe(recipes["butter_toast"])
    dinner.add_recipe(recipes["cheese_pasta"])

    return [breakfast, lunch, dinner]

def create_all_meals():
    ingredients = create_ingredients()
    recipes = create_recipes(ingredients)
    return create_meals(recipes)
