print("Welcome to the Game! Made by Benjamin F., Djuradj P. and Vladylslav B.")
input("Press Enter to start the game...")
def startgame():
    print("Choose a character:")
    n=1
    while n!=0:
        print("")
        print("1. Knight KillALot \n 2. Benjamin \n 3. Djuradj \n 4. Vladyslav")
        int(input("Enter the corresponding number"))
        if n=="1":
            print("Knight KillALot - Attacks with a solid sword and wears a solid armour \n HP: 200 \n AP: 30 \n SKill: Forward Dash - Knight KillALot dashes forward and deals 40AP to a single target. Cooldown: 2 Turns\n")
            input("Enter to continue...")
            Character_choice1 = int(input("Do you want to play as this Character? \n 1. Yes \n 2. No (return to Character selection) "))
            if Character_choice1 == 1:
                print("Game now Loading...")
                n = 0
                maingamestart()
            if Character_choice1 == 2: 
                n = 1
        if n=="2":  
            print("Benjamin - Attacks with an Umbrella and wears a lot of funny clothes \n HP: 275 \n AP: 20 \n SKill: It's reigning! - Benjamin opens his Umbrella and makes acid rain down and deals 35AP to all Enemies. Cooldown: 3 Turns \n")
            input("Press Enter to continue...")
            input("Enter to continue...")
            Character_choice2 = int(input("Do you want to play as this Character? \n 1. Yes \n 2. No (return to Character selection) "))
            if Character_choice2 == 1:
                print("Game now Loading...")
                n = 0
                maingamestart()
            if Character_choice2 == 2: 
                n = 1
        if n=="3":
            print("Djuradj - Attacks with double-wielded Daggers and wears not a lot to show off his muscles \n HP: 150 \n AP: 2x18 \n Skill: Backstepstab - Djuradj jumps over the Enemy and deals 45AP to a single Enemy, stabbing them in the back. Cooldown: 3 Turns \n")
            input("Press Enter to continue...")
            input("Enter to continue...")
            Character_choice3 = int(input("Do you want to play as this Character? \n 1. Yes \n 2. No (return to Character selection) "))
            if Character_choice3 == 1:
                print("Game now Loading...")
                n = 0
                maingamestart()
            if Character_choice3 == 2: 
                n = 1
        if n=="4":
            print("Vladyslav - Attacks with self crafted bombs and wears a simple scientists kit \n HP: 180 \n AP:  ")
            input("Press Enter to continue...")
            input("Enter to continue...")
            Character_choice4 = input("Do you want to play as this Character? \n 1. Yes \n 2. No (return to Character selection) ")
            if Character_choice4 == "1":
                print("Game now Loading...")
                n = 0
                maingamestart()
            if Character_choice4 == "2": 
                n = 1
            else:
                print("We gave you one job, and you failed it. Please try again and choose a number which is either 1 or 2...")
                n = 1
        elif:
            print("Invalid number, try again.")
            input("enter to continue")
def maingamestart():
    import Maingame.py
def Help_start():
    print("This is a short RPG/Dungeon game where you will explore a dungeon, fight monsters, and collect treasures.")
    help_choice = True
    while help_choice = True:
        help_Start_choice = input("If you want to return to the main menu enter 1. \n If you want to see even MORE information enter 2.")
        if help_Start_choice == "1":
            help_choice = False
            startmenu()
        elif help_Start_choice == "2":
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
    while k==0:
        choice_start = input("Select an option: ")
        if choice_start == "1":
            k=1
            startgame()
        if choice_start == "2":
            k=1
            Help_start()
            input("Press Enter to return to the main menu...")
            print("Now returning to main menu...")
            startmenu()
        if choice_start == "3":
            k=1
            exit()
        else:
            k=0
            print("We gave you one job, and you failed it. Please try again and choose a number which is either 1, 2 or 3...")
            
        
startmenu()
