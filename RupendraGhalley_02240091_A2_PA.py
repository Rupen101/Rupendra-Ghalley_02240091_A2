import random

score_guess_game = 0

options = ('rock', 'paper', 'scissors')


least_pokedex = 1
Highest_pokedex = 1025
pokemon_binder = []


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

# Main loop
while True:
    print("Select a function (0-5):")
    print("1. Guess Number game")
    print("2. Rock paper scissors game")
    print("3. Trivia Pursuit Game")
    print("4. Pokemon Card Binder Manager")
    print("0. Exit program")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Guess Number Game")
        target_number = random.randint(1, 100)
        score = 0
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess == target_number:
                print("Correct!")
                score += 10
            else:
                print("Wrong! The number was:", target_number)
        except:
            print("Invalid input. Please enter a number.")
    
    elif choice == 2:
        player = input("Enter rock, paper, or scissors: ").lower()
        score = 0
        computer = random.choice(options)
        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
            (player == "paper" and computer == "rock") or \
            (player == "scissors" and computer == "paper"):
            print("You win!")
            score += 1
        else:
            print("You lose.")

    elif choice == 3:
        Score = 0
        print("Trivia Pursuit Game")
        question = "Who was the first Bhutanese man to climb on the Mt.Everest?\n(a) Jigme Tenzin Sherpa \n(b) Jigme Pelden Dorji\n(c) Jigme Dorji\n"
        answer = input(question + "Your answer: ").lower()
        
        if answer == "b":
            print("Correct!")
            score += 1
        else:
            print("Sorry. The correct answer was b.(Jigme Pelden Dorji).")
            
    elif choice == 4:   
        while True:
            print()
            print("Pokemon Card Binder")
            print("1. Add Pokemon card")
            print("2. Reset binder")
            print("3. View current placements")
            print("4. Exit")
            option = int(input("what are you looking for: "))
        
            if option == 1:
                pokedex = int(input("which podex would you like to add?: "))
                if pokedex < least_pokedex or pokedex >= Highest_pokedex:
                    print("does not exist")
                else:
                    pokemon_binder.append(pokedex)
                    pokemon_binder = bubble_sort(pokemon_binder)  # rearranging the pokedex in ascending order
                print(f"Pokemon binder: {pokemon_binder}")
                
            elif option == 2:
                your_confirmation = input("confirm the command to proceed (yes/no) : ")
                if your_confirmation == "yes":
                    pokemon_binder.clear() 
                    print("Pokemon binder cleared.")
                    print(f"Pokemon binder: {pokemon_binder}")
       
            elif option == 3:
                feature = int(input("1. all\n 2. Selective:  "))
                
                if feature == 1:
                    for i in pokemon_binder:
                        page, row, column = position(i)
                        print(f"Pokedex number: {i}")
                        print(f"Page: {page}")
                        print(f"Row: {row}")
                        print(f"Column: {column}")
                
                elif feature == 2:
                    pokedex = int(input("Enter the pokedex you want to view the placement: "))
                    if pokedex in pokemon_binder:
                        page, row, column = position(pokedex)
                        print(f"Pokedex number: {pokedex}")
                        print(f"Page: {page}")
                        print(f"Row: {row}")
                        print(f"Column: {column}")
            
            else:
                break
                
    elif choice == 0:
        print("Thank you for playing!")
        break
    
    else:
        print("Invalid choice. Please try again.")
