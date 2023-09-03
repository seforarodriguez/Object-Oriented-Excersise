class PettingZoo:
    def __init__(self,name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def adding_animals_to_attraction(self, animal):
        self.animals.append(animal)
    
    @property #getter
    def last_critter_added(self):
        animals = self.animals
        last_one = animals[0].name
        return last_one

class SnakePit:
    def __init__(self,name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def adding_animals_to_attraction(self, animal):
        self.animals.append(animal)

class Wetlands:
    def __init__(self,name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()
    def adding_animals_to_attraction(self, animal):
        self.animals.append(animal)
