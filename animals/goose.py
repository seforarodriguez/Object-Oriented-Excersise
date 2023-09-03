from .animals import Animal
from movements import Walking, Swimming
class Goose(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        Animal.__init__(self, name, species, food, chip_number)
        Swimming.__init__(self)
        Walking.__init__(self)
    def honk(self):
        print("The goose honks. A lot!")
    def __str__(self):
        return f"{self.name} the Most Amazing Goose!"