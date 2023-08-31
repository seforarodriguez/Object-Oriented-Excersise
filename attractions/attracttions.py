class PettingZoo:
    def __init__(self,name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def adding_animals_to_attraction(self, animal):
        self.animals.append(animal)
    
    @property #getter
    def last_critter_added(self):
        reversed_list = self.animals.reverse(self.animals)
        print(f"Last animal added was {reversed_list[0]}")

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
