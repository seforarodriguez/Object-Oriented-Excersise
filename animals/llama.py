from animals import Animal
from movements import Walking
class Llama(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        Animal.__init__(self, name, species, food, chip_number)
        Walking.__init__(self)
        self.shift = shift
    def stare(self):
        print("The Llama gives judgy stares!")
    def __str__(self):
        return f"{self.name} the Most Amazing Judgy Llama"



