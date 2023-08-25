from swimming import Goose, Crocodile, Hippopotamus, Swan, RatSnakes, Flamingos, Copperheads
from slithering import Mallards, Goldfish, Clownfish, Starfish
from walking import Llama, Donkeys, Unicorns, Goats,Burro
from attractions import PettingZoo, SnakePit, Wetlands


# Creation of the different instances for the walking animals

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "Morning", "Llama Chow" )
miss_furry = Goats("Miss Furry", "domestic Goat", "Midday", "Grass" )
mr_fuzzy = Unicorns("Miss Fuzzy", "domestic Unicorn", "Afternoon", "Glitter" )
ms_donke = Donkeys("Miss Donke", "domestic donkey", "Midday", "Donkey food" )

# Instances for the different swimming animals
Freida = Goose("Miss Freida", "domestic llama", "Goose Gummies" )
Lola = Crocodile("Miss Lola", "domestic llama", "Bird Legs" )
mr_Carlo = Hippopotamus("Mr Carlo", "domestic llama", "Hippo Soda" )
miss_carla = Swan("Miss Carla", "domestic llama",  "Swany Cake" )
miss_fuzzy = RatSnakes("Miss Fuzzy", "domestic llama", "Rats" )
breakeba = Flamingos("Miss breakeba", "domestic llama", "Pink Glitter" )
Furr_man = Copperheads("Mr Furr Man", "domestic llama", "Sparkling Watter" )

# Creation of instances for the different slithering animals
miss_fuzzle = Mallards("Miss Fuzzle", "domestic Mallard", "Seaweed")
stinky = Goldfish("Stinky", "savage Goldfish", "Seaweed")
stanky = Clownfish("Stanky", "Nemo's Clownfish", "Seaweed")
kanky = Starfish("Kannky", "Funny Starfish", "Seaweed")

# Creation of instances for the different attractions
varmint_village = PettingZoo("Varmint Village", "the best place to have fun")
varmint_village.adding_animals_to_attraction(miss_fuzz)
varmint_village.adding_animals_to_attraction(miss_furry)
varmint_village.adding_animals_to_attraction(mr_fuzzy)
varmint_village.adding_animals_to_attraction(ms_donke)


snakeru = SnakePit("Snakeru Playground", "The best place to get bitten")
snakeru.adding_animals_to_attraction(Freida)
snakeru.adding_animals_to_attraction(Lola)
snakeru.adding_animals_to_attraction(miss_carla)
snakeru.adding_animals_to_attraction(miss_fuzzy)
snakeru.adding_animals_to_attraction(mr_Carlo)
snakeru.adding_animals_to_attraction(breakeba)
snakeru.adding_animals_to_attraction(Furr_man)

wettingland = Wetlands("Ocean Land", "Best place to play in the Summer")
wettingland.adding_animals_to_attraction(miss_fuzzle)
wettingland.adding_animals_to_attraction(stinky)
wettingland.adding_animals_to_attraction(stanky)
wettingland.adding_animals_to_attraction(kanky)




# for animal in varmint_village.animals:
#     print(f'{varmint_village.attraction_name} is where you will find animals like {animal.name} the {animal.species} in {varmint_village.attraction_name}')

print(f"{varmint_village.attraction_name} is where you will find amazing animals that you can pet such as:")
for animal in varmint_village.animals:
    print(f' * {animal.name} the {animal.species} ')

print(f"{snakeru.attraction_name} is where you will find amazing animals that you can pet such as:")
for animal in snakeru.animals:
    print(f' * {animal.name} the {animal.species}')
    
print(f"{wettingland.attraction_name} is where you will find amazing animals that you can pet such as:")
for animal in wettingland.animals:
    print(f' * {animal.name} the {animal.species}')