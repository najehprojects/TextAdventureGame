import math
import sys
import time
import random
import copy


def wait(secs):
   time.sleep(secs)

skillShop = {

    "skills" : {

        1 : {
            "spcost" : 3,
            "name": "Low Heal",
            "manacost": 45,

            "healamount": 10,
        },

        2 : {
            "spcost" : 3,
            "name": "Slow",
            "manacost": 35,

            "debufftype" : "atk",
            "debuffamount": 5,
            "debuffduration" : 2,
        },

        3 : {
            "spcost" : 3,
            "name": "Slice",
            "manacost": 40,

            "damage" : 25,
        },

        4 : {
            "spcost": 5,
            "name" : "Heal",
            "manacost": 50,

            "healpercentage": 25,
        },

        5 : {
            "spcost": 5,
            "name" : "Poison",
            "manacost": 50,

            "poisondamage": 5,
            "debufftype": "def",
            "debuffamount": 5,
            "debuffduration" : 5,
        },

        6 : {
            "spcost": 5,
            "name" : "Slash",
            "manacost": 50,

            "damage" : 35,
        },

        7 : {
            "spcost": 10,

            "name": "Master Heal",
            "manacost": 75,

            "healpercentage": 50,
        },

        8 : {
            "spcost": 10,

            "name": "Venom",
            "manacost" : 65,

            "damage" : 5,
            "poisondamage" : 10,
            "debufftype" : "def",
            "debuffamount" : 10,
            "debuffduration" : 4,
        },

        9 : {
            "spcost": 10,

            "name": "Execute",
            "manacost": 75,

            "damage" : 65,
        },

    },

}

plr = {
    "name" : "",
    "weapon" : "None",

    "inventory": [""],

    "skils" : [""],

    "level" : 66,
    "xp" : 28710,

    "skillpoints" : 3,

    "atk" : 15,
    "def" : 10,
    "hp" : 100,

    "mana" : 100,

    "title" : " the Hero",


    "scene": "Intro",
    "moves" : 5,
    "pos": 0,

    "dif" : ""
}

critChance = 12
missChance = 5

def gameover():
    print("Game Over")
    exit(0)

def showstats():
    print()
    print("-<{[PLAYER STATS]}>-")
    print()
    print("["+str.upper(plr["name"])+str.upper(plr["title"])+"]")
    print("Current Weapon:", plr["weapon"])
    print("Level:", plr["level"])
    print("XP:", plr["xp"])
    print()

def animatetxt(msg, spd):
    for chara in msg:
        sys.stdout.write(chara)
        sys.stdout.flush()
        wait(0.25/spd)

    print()

animatetxt("Welcome to...",1)
print()
animatetxt(""" .d8888b.  888                                                  8888888     888 d8b          888         888    888                          888 
d88P  Y88b 888                                                    888       888 Y8P          888         888    888                          888 
888    888 888                                                    888       888              888         888    888                          888 
888        88888b.   .d88b.   .d88b.  .d8888b   .d88b.            888   .d88888 888  .d88b.  888888      8888888888  .d88b.  888d888 .d88b.  888 
888        888 "88b d88""88b d88""88b 88K      d8P  Y8b           888  d88" 888 888 d88""88b 888         888    888 d8P  Y8b 888P"  d88""88b 888 
888    888 888  888 888  888 888  888 "Y8888b. 88888888           888  888  888 888 888  888 888         888    888 88888888 888    888  888 Y8P 
Y88b  d88P 888  888 Y88..88P Y88..88P      X88 Y8b.    d8b        888  Y88b 888 888 Y88..88P Y88b.       888    888 Y8b.     888    Y88..88P  "  
 "Y8888P"  888  888  "Y88P"   "Y88P"   88888P'  "Y8888 88P      8888888 "Y88888 888  "Y88P"   "Y888      888    888  "Y8888  888     "Y88P"  888 
                                                       8P                                                                                        
                                                       "                                                                                         
                                                                                                                                                 """, 100)
wait(1)

input("Press enter to continue...")

print("First, please enter a name")
plr["name"] = input()

while plr["name"] == "":
    plr["name"] = input("Enter a valid name: ")

if plr["name"] == "Zeri":
    plr["hp"] = 99999999999999
    plr["atk"] = 99999999999999
    plr["def"] = 99
    plr["level"] = 999
    plr["xp"] = 99999999999999
    plr["weapon"] = "Strong ahh stick"

elif plr["name"] == "Hero":
    animatetxt("So you've chosen this path...", 0.9)
    plr["hp"] = 5
    plr["atk"] = 999
    plr["def"] = 99
    plr["title"] = ", the True Saviour"
    plr["level"] = 999
    plr["weapon"] = "The Legendary Blade, Excalibur"
    wait(3)

showstats()

wait(1)

def difficulty_select():

    print("Choose Your Difficulty")
    plr["dif"] = input("[Easy/Normal/Hard/Impossible] ")

    while plr["dif"].upper() != "EASY" and plr["dif"].upper() != "NORMAL" and plr["dif"].upper() != "HARD" and plr["dif"].upper() != "IMPOSSIBLE" and plr["dif"].upper() != "E" and plr["dif"].upper() != "N" and plr["dif"].upper() != "H" and plr["dif"].upper() != "I":
        plr["dif"] = input("Enter a valid difficulty: ")

    if plr["dif"].upper() == "E":
        plr["dif"] = "EASY"
    if plr["dif"].upper() == "N":
        plr["dif"] = "NORMAL"
    if plr["dif"].upper() == "H":
        plr["dif"] = "HARD"
    if plr["dif"].upper() == "I":
        plr["dif"] = "IMPOSSIBLE"

    plr["dif"] = plr["dif"].upper()
    print("Selected Difficulty "+ plr["dif"])

difficulty_select()

difCon = input("Are you sure you would like to proceed with difficulty "+ plr["dif"]+"? "+ "[Y/N]: ")
while difCon.upper() != "Y":

    while difCon.upper() != "Y" and difCon.upper() != "N":
        difCon = input("Confirm difficulty "+ plr["dif"]+"? "+ "[Y/N]: ")

    if difCon.upper() == "N":
        difficulty_select()
        difCon = ""

doTut = input("Would you like to play the tutorial? [Y/N]: ")
while doTut.upper() != "Y" and doTut.upper() != "N":
    doTut = input("Would you like to play the tutorial? [Y/N]: ")

enemyTemplates = {

    "tutorial" : {
        "titles" : ["Training Dummy"],
        "atk" : 1,
        "def" : 0,
        "hp" : 100,
        "xp" : "tutorial",
        "name" : "",
    },

    "low" : {
        "titles" : ["Goblin", "Green Slime", "Skeleton", "Rotten Zombie", "Wolf"],
        "atk": 1,
        "def": 1,
        "hp": 6,
        "xp" : "low",
        "name" : "",
    },

    "mid" : {
        "titles" : ["Orc", "Blue Slime", "Armored Skeleton", "Zombie", "Wolf Pack Leader"],
        "atk": 7,
        "def": 5,
        "hp": 41,
        "xp" : "mid",
        "name" : "",
    },

    "high": {
        "titles" : ["Orc General", "Red Slime", "Skeleton Warrior", "Mutated Zombie", "Giant"],
        "atk": 15,
        "def": 7,
        "hp": 85,
        "xp" : "high",
        "name" : "",
    },

    "miniboss": {
        "titles" : ["Fenrir", "Giant Black Slime", "Ancient Giant"],
        "atk": 24,
        "def": 12,
        "hp": 150,
        "xp" : "miniboss",
        "name" : "",
    },

    "finalboss": {
        "titles" : ["The Dark Lord"],
        "atk": 50,
        "def": 50,
        "hp": 350,
        "xp" : "finalboss",
        "name" : "",
    },
}

tutorialComplete = False

def battle(enemy):

    currentenemy = copy.deepcopy(enemyTemplates[enemy.lower()])
    currentenemy["name"] = enemyTemplates[enemy.lower()]["titles"][(random.randint(1, len(enemyTemplates[enemy.lower()]["titles"]))) - 1]

    print(plr["name"], "VS.", currentenemy["name"] + "!")

    if enemy.lower() == "tutorial":
        while not tutorialComplete:
            print("Welcome to the Tutorial!")
            break

    while plr["hp"] > 0 and currentenemy["hp"] > 0:

        def action():
            wait(1)
            if (plr["mana"] + 10) <= 100: plr["mana"] += 10
            print("Current Mana:", plr["mana"])
            nextaction = input("Choose your action [ATK - 1 / DEF - 2 / SKILL - 3 / ITEM - 4 / RUN - 5 / ]: ")
            while nextaction.upper() != "ATK" and nextaction.upper() != "DEF" and nextaction.upper() != "RUN" and nextaction != "1" and nextaction != "2" and nextaction != "3":
                nextaction = input("Choose your action [ATK - 1 / DEF - 2 / SKILL - 3 / ITEM - 4 / RUN - 5 / ]: ")
            return nextaction

        def attack(target, damage, skill):

            chance = random.randint(1,100)

            if chance <= critChance:
                damage = damage*(random.randint(2,3))
                print("Critical attack!")

            if chance >= (100-missChance):
                damage = 0
                print("Miss!")

            if skill == 0:
                if target == "plr":
                    plr["hp"] -= math.ceil(damage*(1-(plr["def"]/100)))
                    print("You took", math.ceil(damage*(1-(plr["def"]/100))), "damage!")
                    if plr["hp"] < 0: plr["hp"] = 0
                    print("You have", plr["hp"], "HP left!")
                    print()
                if target == "enemy":
                    currentenemy["hp"] -= math.ceil(damage*(1-(currentenemy["def"]/100)))
                    print("You dealt", math.ceil(damage*(1-(currentenemy["def"]/100))), "damage!")
                    if currentenemy["hp"] < 0: currentenemy["hp"] = 0
                    print(currentenemy["name"], "has", currentenemy["hp"], "HP left!")
                    print()
            if skill == 1:
                print("a")


        def changestat(target, stat, amount):

           if target == "plr":
                plr[stat] += amount

        plrchoice = action()

        cpuchoice = random.randint(1, 2)

        if plrchoice == "ATK" or plrchoice == "1":
            if cpuchoice == 1:
                attack("enemy", plr["atk"], 0)
                wait(1)
                print()
            if cpuchoice == 2:
                if math.ceil(plr["atk"] - currentenemy["def"]) >= 0:
                    attack("enemy", math.ceil(plr["atk"] - currentenemy["def"]), 0)
                    print(currentenemy["name"], "defended! DMG DOWN")
                    wait(1)
                    print()
                else:
                    attack("enemy", 1,0)
                    print(currentenemy["name"], "defended! DMG DOWN")
                    wait(1)
                    print()

        if currentenemy["hp"] >= 1:
            if cpuchoice == 1:
                if plrchoice == "ATK" or plrchoice == "1":
                    attack("plr", currentenemy["atk"], 0)
                    wait(1)
                    print()
                if plrchoice == "DEF" or plrchoice == "2":
                    if math.ceil(currentenemy["atk"] - plr["def"]) >= 0:
                        print("You defended! DMG TAKEN DOWN")
                        attack("plr", math.ceil(currentenemy["atk"] - plr["def"]), 0)
                        wait(1)
                        print()
                    else:
                        print("You defended! DMG TAKEN DOWN")
                        attack("plr", 1, 0)
                        wait(1)
                        print()

        if plrchoice == "2" and cpuchoice == 2 or plrchoice == "DEF" and cpuchoice == 2:
            print("Both Parties Defended! No Damage was taken or dealt!")
            print()

        if plr["hp"] <= 0:
            gameover()
        elif currentenemy["hp"] <= 0:

            print("You win!")
            plr["mana"] = 100
            xpgain = 0

            if currentenemy["xp"].lower() == "tutorial":
                xpgain += 200
            elif currentenemy["xp"].lower() == "low":
                xpgain += random.randint(15, 25)
            elif currentenemy["xp"].lower() == "mid":
                xpgain += random.randint(45, 65)
            elif currentenemy["xp"].lower() == "high":
                xpgain += random.randint(85, 125)
            elif currentenemy["xp"].lower() == "miniboss":
                xpgain += random.randint(200, 400)
            elif currentenemy["xp"].lower() == "finalboss":
                xpgain += 999

            print("You gained:", xpgain, "XP!")
            print()

            oldlevel = plr["level"]

            level = 0
            totalxp = (plr["xp"]+xpgain)

            wait(2)

            if oldlevel < 999:
                while True:
                    if totalxp - (100+(10*level)) >= 0:
                        totalxp -= (100+(10*level))
                        level += 1
                    else:
                        print("XP till next level:",totalxp)
                        break

                if level > oldlevel:
                    print("LEVEL UP!")
                    print("<"+str(oldlevel)+">", "-->", "<"+str(level)+">")
                    print()
                    showstats()
                break
            else:
                print("Level MAX!")

            print()

print("Battle System Tests")

if doTut.upper() == "Y":
    print("Proper Tutorial not yet implemented")
    #battle("Tutorial")

battle("Low")
wait(5)
battle("Mid")
wait(5)
battle("High")
wait(5)
battle("Miniboss")
wait(5)
battle("Low")
wait(5)
battle("Finalboss")