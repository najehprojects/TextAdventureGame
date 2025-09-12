import sys
import time
import random
import os

def wait(secs):
   time.sleep(secs)

plr = {
    "name" : "",
    "weapon" : "None",

    "inventory": [""],

    "level" : 1,
    "xp" : 0,
    "atk" : 4,
    "def" : 1,
    "hp" : 20,

    "scene": "Intro",
    "moves" : 50,
    "pos": 0,

    "dif" : ""
}

def gameover():
    print("Game Over")

def showstats():
    print()
    print("-<{[PLAYER STATS]}>-")
    print()
    print("["+str.upper(plr["name"])+"]")
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

print("Welcome to [Game Title]!")
input("Press enter to continue...")

animatetxt("First, please enter a name:", 2)
plr["name"] = input()

while plr["name"] == "":
    plr["name"] = input("Enter a valid name: ")

showstats()

def difficulty_select():

    animatetxt("Choose Your Difficulty", 3)
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
    animatetxt("Selected Difficulty "+ plr["dif"], 3)

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
        "titles" : "Dummy",
        "atk" : 1,
        "def" : 0,
        "hp" : 999,
    },

    "low" : {
        "titles" : ["Goblin", "Green Slime", "Skeleton", "Rotten Zombie", "Wolf"],
        "atk": 1,
        "def": 1,
        "hp": 6,
    },

    "mid" : {
        "titles" : ["Orc", "Blue Slime", "Armored Skeleton", "Zombie", "Wolf Pack Leader"],
        "atk": 3,
        "def": 3,
        "hp": 12,
    },

    "high": {
        "titles" : ["Orc General", "Red Slime", "Skeleton Warrior", "Mutated Zombie", "Giant"],
        "atk": 5,
        "def": 5,
        "hp": 25,
    },

    "miniboss": {
        "titles" : ["Fenrir", "Giant Black Slime", "Ancient Giant"],
        "atk": 7,
        "def": 7,
        "hp": 35,
    },

    "final_boss": {
        "title" : ["The Dark Lord"],
        "atk": 10,
        "def": 10,
        "hp": 35,
    },
}

def battle(enemy):

    print(plr["name"], "VS.", enemy+"!")

    currentenemy = enemyTemplates[enemy.lower()]

    while plr["hp"] > 0 and currentenemy["hp"] > 0:

        def action():
            nextaction = input("Choose your action [ATK - 1 / DEF - 2 / RUN - 3]: ")
            while nextaction.upper() != "ATK" and nextaction.upper() != "DEF" and nextaction.upper() != "RUN" and nextaction != "1" and nextaction != "2" and nextaction != "3":
                nextaction = input("Choose your action [ATK - 1 / DEF - 2 / RUN - 3]: ")
            return nextaction

        def attack(target, damage):

            chance = random.randint(1,20)

            if chance <= 2:
                damage = damage*(random.randint(2,3))
                print("Critical attack!")

            if chance == 20:
                damage = 0
                print("Miss!")

            if target == "plr":
                plr["hp"] -= damage*(1-(plr["def"]/100))
                print("You took", damage*(1-(plr["def"]/100)), "damage!")
                print("You have", plr["hp"], "HP left!")
                print()
            if target == "enemy":
                currentenemy["hp"] -= damage*(1-(currentenemy["def"]/100))
                print("You dealt", damage*(1-(currentenemy["def"]/100)), "damage!")
                print(currentenemy["titles"], "has", currentenemy["hp"], "HP left!")
                print()

        plrchoice = action()

        if plrchoice == "ATK" or plrchoice == "1":
            attack("enemy", plr["atk"])

        if plr["hp"] <= 0:
            gameover()
        elif currentenemy["hp"] <= 0:

            print("You win!")
            xpgain = 0

            if enemyTemplates[enemy.lower()] == "tutorial":
                xpgain += 0
            elif enemyTemplates[enemy.lower()] == "low":
                xpgain += random.randint(5,15)
            elif enemyTemplates[enemy.lower()] == "mid":
                xpgain += random.randint(15, 25)
            elif enemyTemplates[enemy.lower()] == "high":
                xpgain += random.randint(25, 35)
            elif enemyTemplates[enemy.lower()] == "miniboss":
                xpgain += random.randint(40, 60)
            elif enemyTemplates[enemy.lower()] == "finalboss":
                xpgain += 999

            print("You gained:", xpgain, "XP!")
            break

if doTut.upper() == "Y":
    battle("Tutorial")
