from animals import Goose, Crocodile, Hippopotamus, Swan, RatSnakes, Flamingos, Copperheads
from animals import Mallards, Goldfish, Clownfish, Starfish
from animals import Llama, Donkeys, Unicorns, Goats, Burro
from attractions import PettingZoo, SnakePit, Wetlands


# Creation of the different instances for the walking animals

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "Morning", "Llama Chow", "5559999" )
miss_furry = Goats("Miss Furry", "domestic Goat", "Midday", "Grass", "888888" )
mr_fuzzy = Unicorns("Miss Fuzzy", "domestic Unicorn", "Afternoon", "Glitter", "54854" )
ms_donke = Donkeys("Miss Donke", "domestic donkey", "Midday", "Donkey food","111222" )
ms_donke = Burro("Burrito Sabanero", "savage donkey", "Midday", "Donkey food","222111" )

# Instances for the different swimming animals
Freida = Goose("Miss Freida", "domestic llama", "Goose Gummies","333555" )
Lola = Crocodile("Miss Lola", "domestic llama", "Bird Legs","444555" )
mr_Carlo = Hippopotamus("Mr Carlo", "domestic llama", "Hippo Soda","555666" )
miss_carla = Swan("Miss Carla", "domestic llama",  "Swany Cake","666777" )
miss_fuzzy = RatSnakes("Miss Fuzzy", "domestic llama", "Rats","777888" )
breakeba = Flamingos("Miss breakeba", "domestic llama", "Pink Glitter","888999" )
Furr_man = Copperheads("Mr Furr Man", "domestic llama", "Sparkling Watter","999191" )

# Creation of instances for the different slithering animals
miss_fuzzle = Mallards("Miss Fuzzle", "domestic Mallard", "Seaweed","111191")
stinky = Goldfish("Stinky", "savage Goldfish", "Seaweed","222292")
stanky = Clownfish("Stanky", "Nemo's Clownfish", "Seaweed","333393")
kanky = Starfish("Kannky", "Funny Starfish", "Seaweed","444494")

# Creation of instances for the different attractions
varmint_village = PettingZoo("Varmint Village", "the best place to have fun")
varmint_village.adding_animals_to_attraction(miss_fuzz)
varmint_village.adding_animals_to_attraction(miss_furry)
varmint_village.adding_animals_to_attraction(mr_fuzzy)
varmint_village.adding_animals_to_attraction(ms_donke)

print(varmint_village.last_critter_added)

snakeru = SnakePit("Snakeru Playground", "The best place to get bitten")
snakeru.adding_animals_to_attraction(Lola)
snakeru.adding_animals_to_attraction(miss_carla)
snakeru.adding_animals_to_attraction(miss_fuzzy)
snakeru.adding_animals_to_attraction(mr_Carlo)
snakeru.adding_animals_to_attraction(breakeba)
snakeru.adding_animals_to_attraction(Furr_man)
snakeru.adding_animals_to_attraction(Freida)

wettingland = Wetlands("Ocean Land", "Best place to play in the Summer")
wettingland.adding_animals_to_attraction(miss_fuzzle)
wettingland.adding_animals_to_attraction(stinky)
wettingland.adding_animals_to_attraction(stanky)
wettingland.adding_animals_to_attraction(kanky)




for animal in varmint_village.animals:
    print(f'{varmint_village.attraction_name} is where you will find animals like {animal.name} the {animal.species} in {varmint_village.attraction_name}')

#this is printing all the animals per attraction and showing it in the console with the iteration
print(f"{varmint_village.attraction_name} is where you will find amazing animals that you can pet such as:")
for animal in varmint_village.animals:
    print(animal)

print(f"{snakeru.attraction_name} is where you will find amazing animals that you can pet such as:")
for animal in snakeru.animals:
    print(animal)
    
print(f"{wettingland.attraction_name} is where you will find amazing animals that you can pet such as:")
for animal in wettingland.animals:
    print(animal)


print(miss_fuzz.chip_number)

print("These are the Methods and different examples of the Goose Class")
Freida.run()
Freida.swim()

# This code is iterating through the methods in the Goose Class
methods_in_class = dir(Freida)

for method in methods_in_class:
    print(method)