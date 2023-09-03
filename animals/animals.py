from datetime import date

class Animal:

    def __init__(self, name, species, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species =species
        self.date_added = date.today()
        self.food = food
        self.__chip_number = chip_number

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} the {self.species}."
    
    @property #getter for the chipnumber
    def chip_number(self):
        return self.__chip_number
        
    @chip_number.setter #setter for the chip number
    def chip_number(self, number):
        pass
class Llama(Animal):

    def __init__(self, name, species, shift, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(name, species, food, chip_number)
        self.shift = shift
        self.walking = True   
class Donkeys(Animal):

    def __init__(self, name, species, shift, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(name, species, food, chip_number)
        self.shift = shift
        self.walking = True
class Unicorns(Animal):

    def __init__(self, name, species, shift, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(name, species, food, chip_number)
        self.shift = shift
        self.walking = True
class Goats(Animal):

    def __init__(self, name, species, shift, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(name, species, food, chip_number)
        self.shift = shift
        self.walking = True
class Burro(Animal):

    def __init__(self, name, species, shift, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(name, species, food, chip_number)
        self.shift = shift
        self.walking = True

class Mallards(Animal):

    def __init__(self, name, species, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(name, species, food, chip_number)
        self.slithering = True
class Goldfish(Animal):

    def __init__(self, name, species, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(name, species, food, chip_number)
        self.slithering = True
class Clownfish(Animal):

    def __init__(self, name, species, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(name, species, food, chip_number)
        self.slithering = True
class Starfish(Animal):

    def __init__(self, name, species, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(name, species, food, chip_number)
        self.slithering = True
class Copperheads(Animal):

    def __init__(self, name, species, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(self, name, species, food)
        self.swimming = True
class Flamingos(Animal):

    def __init__(self, name, species, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(self, name, species, food)
        self.swimming = True
class RatSnakes(Animal):

    def __init__(self, name, species, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(self, name, species, food)
        self.swimming = True
class Swan(Animal):

    def __init__(self, name, species, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(self, name, species, food)
        self.swimming = True
class Hippopotamus(Animal):

    def __init__(self, name, species, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(self, name, species, food)
        self.swimming = True
class Crocodile(Animal):

    def __init__(self, name, species, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        super().__init__(self, name, species, food)
        self.swimming = True