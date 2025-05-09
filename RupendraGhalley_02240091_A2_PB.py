import random

# Pokemon_Binder_Game setup
least_pokedex = 1
Highest_pokedex = 1025
pokemon_binder = []

# Sorting helper
def bubble_sort(pokemon_binder):
    n = len(pokemon_binder)
    for i in range(n):
        for j in range(0, n - i - 1):
            if pokemon_binder[j] > pokemon_binder[j + 1]:
                pokemon_binder[j], pokemon_binder[j + 1] = pokemon_binder[j + 1], pokemon_binder[j]
    return pokemon_binder

# Placement helper
def position(num):
    num = num - 1
    page = (num // 64) + 1
    row = ((num % 64) // 8) + 1
    column = ((num % 64) % 8) + 1
    return (page, row, column)

# Main loop for Pokemon Card Binder
while True:
    print("Pokemon Card Binder")
    print("1. Add Pokemon card")
    print("2. Reset binder")
    print("3. View current placements")
    print("4. Exit")
    option = int(input("What are you looking for: "))
    
    if option == 1:
        pokedex = int(input("Which pokedex would you like to add?: "))
        if pokedex < least_pokedex or pokedex >= Highest_pokedex:
            print("Pokedex number does not exist.")
        else:
            pokemon_binder.append(pokedex)
            pokemon_binder = bubble_sort(pokemon_binder)  # rearranging the pokedex in ascending order
        print(f"Pokemon binder: {pokemon_binder}")
    
    elif option == 2:
        your_confirmation = input("Confirm the command to proceed (yes/no): ")
        if your_confirmation == "yes":
            pokemon_binder.clear() 
            print("Pokemon binder cleared.")
            print(f"Pokemon binder: {pokemon_binder}")
    
    elif option == 3:
        feature = int(input("1. All\n2. Selective: "))
        
        if feature == 1:
            for i in pokemon_binder:
                page, row, column = position(i)
                print(f"Pokedex number: {i}")
                print(f"Page: {page}")
                print(f"Row: {row}")
                print(f"Column: {column}")
        
        elif feature == 2:
            pokedex = int(input("Enter the pokedex you want to view the placement for: "))
            if pokedex in pokemon_binder:
                page, row, column = position(pokedex)
                print(f"Pokedex number: {pokedex}")
                print(f"Page: {page}")
                print(f"Row: {row}")
                print(f"Column: {column}")
    
    elif option == 4:
        print("Thank you for using the Pokemon Card Binder!")
        break
    
    else:
        print("Invalid option. Please try again.")
