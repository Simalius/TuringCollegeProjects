import pytest
from ingredients import Ingredient

def test_ingredient_initialization():
    ingredient = Ingredient("Tomato", 100, "grams", 2.0)
    assert ingredient.name == "Tomato"
    assert ingredient.quantity == 100
    assert ingredient.unit == "grams"
    assert ingredient.calories_per_unit == 2.0

def test_total_calories():
    ingredient = Ingredient("Tomato", 100, "grams", 2.0)
    assert ingredient.total_calories() == 200.0

def test_str_method():
    ingredient = Ingredient("Tomato", 100, "grams", 2.0)
    assert str(ingredient) == "100 grams of Tomato (200.0 calories)"
