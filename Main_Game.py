import random

import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Qiqi2009",
    database ="game_database"
)
if connection.is_connected():
    print("Successfully connected to the database")
else: 
    print("Connection to database failed")
pot_inventory = {
    1:0,
    2:0, 
    3:0, 
    4:0, 
    5:0
}
print("Welcome to the Game! Made by Benjamin F., Djuradj P. and Vladylslav B.")
input("Press Enter to start the game...")
def startgame():
    print("Choose a character:")
    print("")
    print("1. Knight KillALot \n2. Benjamin \n3. Djuradj \n4. Vladyslav")
    Character_choice_start = input("Enter the corresponding number: ")
    if Character_choice_start == "1":
        print("Knight KillALot - Attacks with a solid sword and wears a solid armour \n HP: 200 \n AP: 30 \n SKill: Forward Dash - Knight KillALot dashes forward and deals 40AP to a single target. Cooldown: 2 Turns\n")
        input("Enter to continue...")
        print("Do you want to play as this Character? \n 1. Yes \n 2. No (return to Character selection) ")
        Character_choice = input("Enter your choice: ")
        if Character_choice == "1":
            character_number = int(Character_choice_start)
            print("Game now Loading...")
            return character_number
        if Character_choice == "2": 
            startgame()
        else:
            print("We gave you one job, and you failed it. Please try again and choose a number which is either 1 or 2 next time.")
            startgame()
    if Character_choice_start == "2":
        print("Benjamin - Attacks with an Umbrella and wears a lot of funny clothes \n HP: 275 \n AP: 20 \n SKill: It's reigning! - Benjamin opens his Umbrella and makes acid rain down and deals 35AP to all Enemies. Cooldown: 3 Turns \n")
        input("Enter to continue...")
        print("Do you want to play as this Character? \n 1. Yes \n 2. No (return to Character selection) ")
        Character_choice = input("Enter your choice: ")
        if Character_choice == "1":
            character_number = int(Character_choice_start)
            print("Game now Loading...")
            return character_number
        if Character_choice == "2": 
            startgame()
        else:
            print("We gave you one job, and you failed it. Please try again and choose a number which is either 1 or 2 next time.")
            startgame()
    if Character_choice_start == "3":
        print("Djuradj - Attacks with dual-wielding-Daggers and wears not a lot to show off his muscles \n HP: 150 \n AP: 2x18 \n Skill: Backstepstab - Djuradj jumps over the Enemy and deals 45AP to a single Enemy, stabbing them in the back. Cooldown: 3 Turns \n")
        input("Enter to continue...")
        print("Do you want to play as this Character? \n 1. Yes \n 2. No (return to Character selection) ")
        Character_choice = input("Enter your choice: ")
        if Character_choice == "1":
            character_number = int(Character_choice_start)
            print("Game now Loading...")
            return character_number
        if Character_choice == "2": 
            startgame()
        else:
            print("We gave you one job, and you failed it. Please try again and choose a number which is either 1 or 2 next time.")
            startgame()
    if Character_choice_start == "4":
        print("Vladyslav - Attacks with self crafted bombs and wears a simple scientists kit \n HP: 180 \n AP: 15 (Splash Area:3x3) \n SKill: Physicist's Stone - Vladyslav throws a giant Bomb at the enemies and deals 50AP to every Enemy. Cooldown: 3 Turns \n")
        input("Enter to continue...")
        print("Do you want to play as this Character? \n 1. Yes \n 2. No (return to Character selection) ")
        Character_choice = input("Enter your choice: ")
        if Character_choice == "1":
            character_number = int(Character_choice_start)
            print("Game now Loading...")
            return character_number
        if Character_choice == "2": 
            startgame()
        else:
            print("We gave you one job, and you failed it. Please try again and choose a number which is either 1 or 2 next time.")
            startgame()
    else:
        print("Invalid number, try again.")
        input("Enter to continue")
        startgame()
def Help_start():
    print("This is a short RPG/Dungeon game where you will explore a dungeon, fight monsters, and collect treasures.")
    help_choice = True
    while help_choice == True:
        help_Start_choice = input("If you want to return to the main menu enter 1 \nIf you want to see even MORE information enter 2 \nYour choice: ")
        if help_Start_choice == "1":
            help_choice = False
            return startmenu()
        elif help_Start_choice == "2":
            help_choice = False
            Help_extreme()
        else:
            input("Please choose a fitting number")
            help_choice = True
def Help_extreme():
    print("Overall this game is a simple Dungeon game made by three inexperienced students.")
    input("Press Enter to continue...")
    print("You can choose a Character Class that has different HP, AP and a special SKill that deals a lot of AP at once.")
    input("Press Enter to continue...")
    print("HP is the amount of Health you have.\nAP is the amount of Damage you do. If Enemies deal 20 Damage to you then you will lose 20 Health. (If you don't have an armor that gives defense)")
    input("Press Enter to continue...")
    print("In the caves you will have multiple Encounters. With Encounter you can either find a piece of armor, a weapon, an item or you can encounter an Enemy.")
    input("Press Enter to continue...")
    print("When you encounter an enemy you can have different things you can choose from when its your turn. You can either Attack (Turn ends after), use an Item (Turn ends after), cast a Skill (Turn ends after) or inspect your Inventory (Turn does NOT end)")
    input("Press Enter to continue...")
    print("After enough Encounters you will meet the Boss, he has more HP and after beating him you beat the game!!")
    print("\nIf you're still confused you can read it again after returning to the Main Menu.")
    input("Press Enter to return to the Main Menu...")
    return startmenu()
def exit():
    print("Exiting the game. Goodbye!")
    quit()
def startmenu(): 
    print("1. Start Game")
    print("2. Infos about the game")
    print("3. Exit :(")
    k = 0
    while k == 0:
        choice_start = input("Select an option: ")
        if choice_start == "1":
            k=1
            print("Character Screen loading")
            return startgame()
        if choice_start == "2":
            k=1
            Help_start()
        if choice_start == "3":
            k=1
            exit()
        else:
            print("We gave you one job, and you failed it. Please try again and choose a number which is either 1, 2 or 3...")
def inventory():
    inventory_choice = input("1. Armor \n2. Weapon \n3. Items \n4. Exit Inventory \nYour choice: ")
    if inventory_choice == "1":
        print("This is your current Armor:")
        cur = connection.cursor()
        cur.execute("Select Armor_Name, Armor_HP from Armor where Armor_ID = %s", (Armor_ID,))
        armor_info_p = cur.fetchall()
        armor_info = armor_info_p[0]
        print("Armor Name:", armor_info[0], " \nArmor HP:", armor_info[1])
        input("Press Enter to return to Inventory Menu...")
        inventory()
    elif inventory_choice == "2":
        print("This is your current Weapon:")
        cur = connection.cursor()
        cur.execute("Select Weapon_Name, Weapon_AP, Skill_Name, Skill_AP, Skill_Cooldown from weapons inner join Skills on weapons.Weapon_Skill_ID = Skills.Skill_ID where Weapon_ID = %s", (Weapon_ID,))
        weapon_info_p = cur.fetchall()
        weapon_info = weapon_info_p[0]
        print("Weapon Name:", weapon_info[0], " \nWeapon AP:", weapon_info[1], " \nWeapon Skill:", weapon_info[2], " \nSkill AP:", weapon_info[3], " \nSkill Cooldown:", weapon_info[4])
        input("Press Enter to return to Inventory Menu...")
        inventory()
    elif inventory_choice == "3":
        cur = connection.cursor()
        potion_inventory(cur, pot_inventory)
    elif inventory_choice == "4":
        print("Exiting Inventory...")
    else: 
        print("Invalid choice, please try again.")
        inventory()
def potion_pick_up():
    print("You found a Potion!")
    pot_cur = connection.cursor()
    pot_cur.execute("Select MIN(Item_ID), MAX(Item_ID) from Items")
    min_id, max_id = pot_cur.fetchone()
    pot_id = random.randint(min_id, max_id)
    pot_cur.execute("Select Item_Name, Item_Heal, Item_AP, Item_Duration from Items where Item_ID = %s", (pot_id,))
    potion = pot_cur.fetchone()
    print("You found a", potion[0], "\n It heals: ", potion[1], "\n It gives extra AP: ", potion[2], "\n It lasts for:", potion[3], "turns.")
    input("Press Enter to continue your journey...")
    potion_inventory_add(pot_inventory, pot_id)
def potion_inventory_add(pot_inventory, pot_id):
    pot_inventory[pot_id] = pot_inventory.get(pot_id, 0) + 1
def potion_inventory(cursor, pot_inventory):
    print("These are your current Items:")
    for pot_id, count in pot_inventory.items():
        cursor.execute("SELECT Item_Name FROM Items WHERE Item_ID = %s", (pot_id,))
        item_name = cursor.fetchone()[0]
        print(f"{item_name}: {count}")
    input("Press Enter to return to Inventory Menu...")
    inventory()
def weapon_pick_up():
    print("You found a Weapon!")
    weapon_cur = connection.cursor()
    weapon_cur.execute("Select MIN(Weapon_ID), MAX(Weapon_ID) from weapons")
    min_id, max_id = weapon_cur.fetchone()
    weapon_id = random.randint(min_id, max_id)
    weapon_cur.execute("Select Weapon_Name, Weapon_AP, Skill_Name, Skill_AP, Skill_Cooldown from weapons inner join Skills on weapons.Weapon_Skill_ID = Skills.Skill_ID where Weapon_ID = %s", (weapon_id,))
    weapon_found = weapon_cur.fetchone()
    weapon_inventory_add(weapon_found, weapon_id)
def weapon_inventory_add(weapon_found, weapon_id):
    print("You found: ", weapon_found[0], "\n It has AP:", weapon_found[1], "\n It has Skill:", weapon_found[2], "\n Skill AP:", weapon_found[3], "\n Skill Cooldown:", weapon_found[4])
    weapon_pick_up_choice = input("Do you want to equip this Weapon? \n 1. Yes \n 2. No (keep current Weapon) \n 3. View Inventory \n Your choice: ")
    if weapon_pick_up_choice == "1":
        global Weapon_ID
        Weapon_ID = weapon_id
        print("You have equipped the new Weapon!")
        input("Press Enter to continue your journey...")
    if weapon_pick_up_choice == "2":
        print("You decided to keep your current Weapon.")
        input("Press Enter to continue your journey...")
    if weapon_pick_up_choice == "3":
        inventory()
        weapon_inventory_add(weapon_found, weapon_id)
def armor_pick_up():
    print("You found Armor!")
    armor_cur = connection.cursor()
    armor_cur.execute("Select MIN(Armor_ID), MAX(Armor_ID) from Armor")
    min_id, max_id = armor_cur.fetchone()
    armor_id = random.randint(min_id, max_id)
    armor_cur.execute("Select Armor_Name, Armor_HP from Armor where Armor_ID = %s", (armor_id,))
    armor_found = armor_cur.fetchone()
    armor_inventory_add(armor_found, armor_id)
def armor_inventory_add(armor_found, armor_id):
    print("You found: ", armor_found[0], "\n It has HP:", armor_found[1])
    armor_pick_up_choice = input("Do you want to equip this Armor? \n 1. Yes \n 2. No (keep current Armor) \n 3. View Inventory \n Your choice: ")
    if armor_pick_up_choice == "1":
        global Armor_ID
        Armor_ID = armor_id
        print("You have equipped the new Armor!")
        input("Press Enter to continue your journey...")
    if armor_pick_up_choice == "2":
        print("You decided to keep your current Armor.")
        input("Press Enter to continue your journey...")
    if armor_pick_up_choice == "3":
        inventory()
        armor_inventory_add(armor_found, armor_id)
def enemy_pick_up():
    print("You encountered an Enemy!")
    enemy_cur = connection.cursor()
    enemy_cur.execute("Select MIN(Enemy_ID), MAX(Enemy_ID) from Enemies")
    min_id, max_id = enemy_cur.fetchone()
    enemy_id = random.randint(min_id, max_id)
    enemy_cur.execute("Select Enemy_Name, Enemy_HP, Enemy_AP from Enemies where Enemy_ID = %s", (enemy_id,))
    enemy_found = enemy_cur.fetchone()
    print("You encountered: ",enemy_found[0], "\n It has HP:", enemy_found[1], "\n It has AP:", enemy_found[2])
    enemy_fight(enemy_found)
def enemy_fight(enemy_found):
    enemy_HP = enemy_found[1]
    Fight_cur = connection.cursor()
    Fight_cur.execute("Select Weapon_AP from weapons where Weapon_ID = %s", (Weapon_ID,))
    Fight_AP = Fight_cur.fetchone()[0]
    Your_AP = Fight_AP
    Fight_cur.execute("Select Armor_HP from Armor where Armor_ID = %s", (Armor_ID,))
    Fight_HP = Fight_cur.fetchone()[0]
    Your_HP = Fight_HP
    Fight_cur.execute("Select Skill_Cooldown from Skills where Skill_ID = %s", (Skill_ID,))
    Skill_Cooldown_Default = Fight_cur.fetchone()[0]
    Skill_Cooldown = 0
    Bonus_AP = 0
    Turn = 0
    move_valid = False
    while enemy_HP > 0:
        Turn += 1
        print("Turn: ", Turn)
        if Skill_Cooldown > 0:
            Skill_Cooldown -= 1
        if Bonus_AP > 0:
            Bonus_AP = 0
        print("Your HP:", Your_HP,"/",Fight_HP,"| Enemy HP:", enemy_HP,"/",enemy_found[1])
        move_valid = False
        input("Press Enter to choose your move...")
        while move_valid == False:
            move = input("Choose your move: \n 1. Attack \n 2. Use Item \n 3. Use Skill \n 4. View Inventory \n Your choice: ")
            if move == "1":
                print("You attacked the enemy for", Your_AP + Bonus_AP, "AP!")
                enemy_HP = enemy_HP - Your_AP - Bonus_AP
                print("Enemy HP left:", enemy_HP)
                move_valid = True
                input("Press Enter to continue...")
                if enemy_HP <= 0:
                    print("You defeated the enemy!")
                    input("Press Enter to continue your journey...")
                    return
            if move == "2":
                cursor = connection.cursor()
                print("These are your current Items:")
                for pot_id, count in pot_inventory.items():
                    cursor.execute("SELECT Item_Name FROM Items WHERE Item_ID = %s", (pot_id,))
                    item_name = cursor.fetchone()[0]
                    print(f"{item_name}: {count}")
                item_fight_choice = input("Enter the number of the item you want to use: ")
                if item_fight_choice.isdigit():
                    item_fight_choice = int(item_fight_choice)
                    if pot_inventory.get(item_fight_choice, 0) > 0:
                        pot_inventory[item_fight_choice] -= 1
                        cursor.execute("SELECT Item_Heal, Item_AP, Item_Duration FROM Items WHERE Item_ID = %s", (item_fight_choice,))
                        item_effects = cursor.fetchone()
                        heal_amount, ap_bonus, duration = item_effects
                        if heal_amount > 0:
                            print(f"You used the item and healed for {heal_amount} HP!")
                            Your_HP += heal_amount
                            move_valid = True
                            input("Press Enter to continue...")
                            if Your_HP > Fight_HP:
                                Your_HP = Fight_HP
                        if ap_bonus > 0:
                            Bonus_AP += ap_bonus
                            print(f"You used the item and gained {ap_bonus} AP for {duration} turns!")
                            move_valid = True
                            input("Press Enter to continue...")
                    else:
                        print("You don't have that item.")
                else:
                    print("Invalid input.")
            if move == "3":
                skill_cur = connection.cursor()
                skill_cur.execute("Select Skill_Name, Skill_AP, Skill_Cooldown from Skills inner join weapons on Skills.Skill_ID = weapons.Weapon_Skill_ID where Weapon_ID = %s", (Weapon_ID,))
                skills = skill_cur.fetchone()
                if Skill_Cooldown == 0:
                    print("You used your skill:", skills[0])
                    enemy_HP = enemy_HP - skills[1]
                    Skill_Cooldown = Skill_Cooldown_Default
                    move_valid = True
                    input("Press Enter to continue...")
                else:
                    print("Your skill is on cooldown for", Skill_Cooldown, "more turns.")
            if move == "4":
                inventory()
            else:
                print("Invalid move, please try again.")
            if enemy_HP > 0 and move_valid == True:
                print("Enemies Turn!")
                print("The enemy attacked you for", enemy_found[2], "AP!")
                input("Press Enter to continue...")
                Your_HP = Your_HP - enemy_found[2]
                print("You have", Your_HP, "HP left.")
                input("Press Enter to continue...")
                if Your_HP <= 0:
                    Your_HP = 0
                    print("You have", Your_HP, "HP left.")
                    print("You have been defeated by the enemy. Game Over.")
                    exit()
    print("You have defeated the enemy!")
    print("You rest up and recover to full health")
    input("Press Enter to continue your journey...")        
def encounter():
    for encounter_number in range(1, 7):
        print(f"Encounter number: {encounter_number}")
        encounter_type = [1, 2, 3, 4]
        encounter_weigh = [1, 1, 2, 1]
        encounter_choice = random.choices(encounter_type, weights=encounter_weigh, k=1)[0]
        if encounter_choice == 1:
            armor_pick_up()
        if encounter_choice == 2:
            weapon_pick_up()
        if encounter_choice == 3:
            enemy_pick_up()
        if encounter_choice == 4:
            potion_pick_up()
    print("You have reached the end of the dungeon for now")
character_stats_number = startmenu()
Armor_ID = character_stats_number
Weapon_ID = character_stats_number
Skill_ID = Weapon_ID

encounter()
