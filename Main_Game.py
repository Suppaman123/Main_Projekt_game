print("Welcome to the Game! Made by Benjamin F., Djuradj P. and Vladylslav B.")
input("Press Enter to start the game...")
def startgame():
    print("You are now able to choose a character. There are 3 in total, let us introduce them:"
    n=1
    while n!=0:
        print("Press a number 1-3 to see the character information, and 0 to choose one.")
        input("Your number...")
        if n=="1":  
            print("The first one is Benjamin a gentleman, who starts with an armour and an umbrella, he has a lot of defence.")
            input("Press Enter to continue...")
        if n=="2":
            print("The second one is Djuradj an assasin, who starts with 2 daggers and deals a lot of damage.")
            input("Press Enter to continue...")
        if n=="3":
            print("The third one is Vladyslav a scientist, who starts with a big brain and has a lot of skills.")
            input("Press Enter to continue...")
        if n=="0":
            print("Now press a number 1-3 to choose a character.")
            class_choice="0"
            while class_choice!="1" and class_choice!="2" and class_choice!="3":
                class_choice = input("Choose your character 1-Benjamin, 2-Djuradj, 3-Vladyslav:...")
                if class_choice!="1" and class_choice!="2" and class_choice!="3":
                    print("invalid number, try again.")
class_choice=int(class_choice)
return class_choice
    input("Press Enter to return to the Main Menu...")
def Help_start():
    print("This is a short RPG/Dungeon game where you will explore a dungeon, fight monsters, and collect treasures.")
    help_choice = True
    while help_choice = True:
        help_Start_choice = int(input("If you want to return to the main menu enter 1. \n If you want to see even MORE information enter 2.")
        if help_Start_choice == 1:
            help_choice = False
            startmenu()
        elif help_Start_choice == 2:
            help_choice = False
            Help_extreme()
        else:
            help_choice = True
def Help_extreme():
   print("Overall this game is a simple Dungeon game made by three inexperienced students.")
   input("Press Enter to continue...")
   print("You can choose a Character Class that has different HP, AP and a special SKill that deals a lot of AP at once.")
   input("Press Enter to continue...")
   print("HP is the amount of Health you have.\n AP is the amount of Damage you do. Enemies that deal 20 Damage to you then you will lose 20 Health. (If you don't have an armor that gives defense)")
   input("Press Enter to continue...")
   print("In the caves you will have multiple Encounters. With Encounter you can either find a piece of armor, a weapon, an item or you can encounter an Enemy.")
   input("Press Enter to continue...")
   print("When you encounter an enemy you can have different things you can choose from when its your turn. You can either Attack (Turn ends after), use an Item (Turn ends after), cast a Skill (Turn ends after) or inspect your Inventory (Turn does NOT end)")
   input("Press Enter to continue...")
   print("After enough Encounters you will meet the Boss, he has more HP and after beating him you beat the game!!")
   print("\n If you're still confused you can read it again after returning to the Main Menu.")
   input("Press Enter to return to the Main Menu...")
   startmenu()
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
def choose_character():
    
