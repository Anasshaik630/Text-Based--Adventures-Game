def start_game():
    print("Welcome to the mystical land of Eldoria, a place filled with wonder and danger.")
    print("You are an adventurer seeking the legendary treasure hidden deep within the enchanted forest.")
    print("Your journey begins now.")
    print()
    first_room()

def first_room():
    print("You find yourself at the edge of the forest. To the north, the trees become denser.")
    print("There is a path leading east and a dark cave to the west.")
    print()
    action = input("What do you do? (north/east/west/look): ").strip().lower()

    if action == "north":
        dense_forest()
    elif action == "east":
        path_east()
    elif action == "west":
        dark_cave()
    elif action == "look":
        look_around()
    else:
        print("Invalid action. Try again.")
        first_room()

def dense_forest():
    print("You venture into the dense forest. The trees tower above you, and it's difficult to see the sky.")
    print("After walking for a while, you find a small clearing with a sparkling stream.")
    print()
    action = input("What do you do? (drink water/look around/back): ").strip().lower()

    if action == "drink water":
        print("The water is refreshing, and you feel rejuvenated.")
        dense_forest()
    elif action == "look around":
        print("You see some berries on a nearby bush and a narrow path leading further into the forest.")
        dense_forest()
    elif action == "back":
        first_room()
    else:
        print("Invalid action. Try again.")
        dense_forest()

def path_east():
    print("You follow the path east and find yourself at a quaint village. The villagers seem friendly.")
    print()
    action = input("What do you do? (talk to villagers/look around/back): ").strip().lower()

    if action == "talk to villagers":
        print("The villagers share stories of the legendary treasure and offer you supplies for your journey.")
        path_east()
    elif action == "look around":
        print("You notice a market with various goods and a blacksmith's shop.")
        path_east()
    elif action == "back":
        first_room()
    else:
        print("Invalid action. Try again.")
        path_east()

def dark_cave():
    print("You enter the dark cave. It's cold and damp, and you can hear the sound of dripping water.")
    print()
    action = input("What do you do? (explore/look around/back): ").strip().lower()

    if action == "explore":
        print("As you explore deeper into the cave, you find a treasure chest filled with gold and jewels!")
        print("Congratulations, you've found the legendary treasure!")
        end_game()
    elif action == "look around":
        print("You see some old carvings on the cave walls and a faint light deeper inside.")
        dark_cave()
    elif action == "back":
        first_room()
    else:
        print("Invalid action. Try again.")
        dark_cave()
def look_around():
    print("You see the dense forest to the north, the path to the east, and the dark cave to the west.")
    first_room()

def end_game():
    print("Thank you for playing! Your adventure has come to an end.")

# Start the game
start_game()
