print("Welcome to the Game! Made by Benjamin F., Djuradj P. and Vladylslav B.")
input("Press Enter to start the game...")
def startgame():
    class_choice = int(input("Choose your class:\n1. Warrior\n2. Mage\n3. Archer\nSelect an option:"))
def Help_start():
    print("This is a short RPG/Dungeon game where you will explore a dungeon, fight monsters, and collect treasures.")    
def exit():
    print("Exiting the game. Goodbye!")
    quit()
def startmenu(): 
    print("1. Start Game (under construction, dont choose)")
    print("2. Infos about the game")
    print("3. Exit :(")
    choice_start = int(input("Select an option: "))
    if choice_start == 1:
        startgame()
    if choice_start == 2:
        Help_start()
        input("Press Enter to return to the main menu...")
        print("Now returning to main menu...")
        startmenu()
    if choice_start == 3:
        exit()
startmenu()
