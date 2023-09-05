from animals import Goose, Crocodile, Hippopotamus, Swan, RatSnakes, Flamingos, Copperheads
from animals import Mallards, Goldfish, Clownfish, Starfish
from animals import Llama, Donkeys, Unicorns, Goats, Burro
from attractions import PettingZoo, WetLands, SnakePit


# Creation of the different instances for the walking animals

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "Morning", "Llama Chow", "5559999" )
miss_furry = Goats("Miss Furry", "domestic Goat", "Midday", "Grass", "888888" )
mr_fuzzy = Unicorns("Miss Fuzzy", "domestic Unicorn", "Afternoon", "Glitter", "54854" )
ms_donke = Donkeys("Miss Donke", "domestic donkey", "Midday", "Donkey food","111222" )
ms_donke = Burro("Burrito Sabanero", "savage donkey", "Midday", "Donkey food","222111" )

# Instances for the different swimming animals
mr_Carlo = Hippopotamus("Mr Carlo", "domestic hippo", "Hippo Soda","555666" )
miss_carla = Swan("Miss Carla", "domestic Swany",  "Swany Cake","666777" )
miss_fuzzy = RatSnakes("Miss Fuzzy", "domestic RatSnake", "Rats","777888" )
breakeba = Flamingos("Miss breakeba", "Pink Flamingo", "Pink Glitter","888999" )
Furr_man = Copperheads("Mr Furr Man", "domestic Copperhead", "Sparkling Watter","999191" )
Lola = Crocodile("Miss Lola", "domestic Croc", "Bird Legs","444555" )
Freida = Goose("Miss Freida", "the Wild Goose", "Goose Gummies","333555" )

# Creation of instances for the different slithering animals
miss_fuzzle = Mallards("Miss Fuzzle", "domestic Mallard", "Seaweed","111191")
stinky = Goldfish("Stinky", "savage Goldfish", "Seaweed","222292")
stanky = Clownfish("Stanky", "Nemo's Clownfish", "Seaweed","333393")
kanky = Starfish("Kannky", "Funny Starfish", "Seaweed","444494")

# Creation of instances for the different attractions
varmint_village = PettingZoo("Varmint Village", "the best place to have fun")
varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(miss_furry)
varmint_village.add_animal(mr_fuzzy)
varmint_village.add_animal(ms_donke)

print(varmint_village.last_critter_added)

snakeru = SnakePit("Snakeru Playground", "The best place to get bitten")
snakeru.add_animal(Lola)
snakeru.add_animal(miss_carla)
snakeru.add_animal(miss_fuzzy)
snakeru.add_animal(mr_Carlo)
snakeru.add_animal(breakeba)
snakeru.add_animal(Furr_man)
snakeru.add_animal(Freida)

wettingland = WetLands("Ocean Land", "Best place to play in the Summer")
wettingland.add_animal(miss_fuzzle)
wettingland.add_animal(stinky)
wettingland.add_animal(stanky)
wettingland.add_animal(kanky)




# for animal in varmint_village.animals:
#     print(f'{varmint_village.attraction_name} is where you will find animals like {animal.name} the {animal.species} in {varmint_village.attraction_name}')


# print(f"{snakeru.attraction_name} is where you will find amazing animals that you can pet such as:")
# for animal in snakeru.animals:
#     print(animal)
    
# print(f"{wettingland.attraction_name} is where you will find amazing animals that you can pet such as:")
# for animal in wettingland.animals:
#     print(animal)


# print(miss_fuzz.chip_number)

# print("These are the Methods and different examples of the Goose Class")
# Freida.run()
# Freida.swim()

# # This code is iterating through the methods in the Goose Class
# methods_in_class = dir(Freida)

# for method in methods_in_class:
#     print(method)

# remember, some animals may require more arguments than others; e.g. shift
dolly = Llama("Dolly", "miniature llama", "morning", "hay", 1033)
snappy = Crocodile("Snappy", "American Alligator", "fish", 1044)

varmint_village.add_animal_pythonic(dolly)
varmint_village.add_animal_type_check(dolly)
varmint_village.add_animal_pythonic(snappy)

#this is printing all the animals per attraction and showing it in the console with the iteration
print(f"{varmint_village.attraction_name} is where you will find amazing animals that you can pet such as:")
for animal in varmint_village.animals:
    print(animal)
