class Ingredient:

    def __init__(self, name, quantity, unit, calories_per_unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.calories_per_unit = calories_per_unit

    def total_calories(self):
        return self.quantity * self.calories_per_unit

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.name} ({self.total_calories()} calories)"
