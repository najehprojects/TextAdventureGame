import math
import sys
import time
import random
import os

from fontTools.subset.svg import xpath
from fontTools.t1Lib import std_subrs


def wait(secs):
   time.sleep(secs)

plr = {
    "name" : "",
    "weapon" : "None",

    "inventory": [""],

    "level" : 67,
    "xp" : 29480,
    "atk" : 15,
    "def" : 10,
    "hp" : 100,


    "scene": "Intro",
    "moves" : 50,
    "pos": 0,

    "dif" : ""
}

theoryxp= 0

for i in range(1,68):
    theoryxp += 100+(10*i)

print(theoryxp)

critChance = 12
missChance = 5

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

print("First, please enter a name")
plr["name"] = input()

while plr["name"] == "":
    plr["name"] = input("Enter a valid name: ")

showstats()

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
        "titles" : "Dummy",
        "atk" : 1,
        "def" : 0,
        "hp" : 20,
        "xp" : "tutorial",
    },

    "low" : {
        "titles" : ["Goblin", "Green Slime", "Skeleton", "Rotten Zombie", "Wolf"],
        "atk": 1,
        "def": 1,
        "hp": 6,
        "xp" : "low",
    },

    "mid" : {
        "titles" : ["Orc", "Blue Slime", "Armored Skeleton", "Zombie", "Wolf Pack Leader"],
        "atk": 3,
        "def": 3,
        "hp": 12,
        "xp" : "mid",
    },

    "high": {
        "titles" : ["Orc General", "Red Slime", "Skeleton Warrior", "Mutated Zombie", "Giant"],
        "atk": 5,
        "def": 5,
        "hp": 25,
        "xp" : "high",
    },

    "miniboss": {
        "titles" : ["Fenrir", "Giant Black Slime", "Ancient Giant"],
        "atk": 7,
        "def": 7,
        "hp": 35,
        "xp" : "miniboss",
    },

    "final_boss": {
        "title" : ["The Dark Lord"],
        "atk": 10,
        "def": 10,
        "hp": 35,
        "xp" : "finalboss",
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

            chance = random.randint(1,100)

            if chance <= critChance:
                damage = damage*(random.randint(2,3))
                print("Critical attack!")

            if chance == (100-missChance):
                damage = 0
                print("Miss!")

            if target == "plr":
                plr["hp"] -= math.ceil(damage*(1-(plr["def"]/100)))
                print("You took", math.ceil(damage*(1-(plr["def"]/100))), "damage!")
                print("You have", plr["hp"], "HP left!")
            if target == "enemy":
                currentenemy["hp"] -= math.ceil(damage*(1-(currentenemy["def"]/100)))
                print("You dealt", math.ceil(damage*(1-(currentenemy["def"]/100))), "damage!")
                print(currentenemy["titles"], "has", currentenemy["hp"], "HP left!")
                print()

        def changestat(target, stat, changing, amount):

            if target == "enemy":
                if changing == "percent":
                    currentenemy[stat] = currentenemy[stat] * (amount/100)
                else:
                    currentenemy[stat] += amount
            elif target == "plr":
                if changing == "percent":
                    plr[stat] = plr[stat] * (amount/100)
                else:
                    plr[stat] += amount



        plrchoice = action()

        cpuchoice = random.randint(1, 2)

        if plrchoice == "ATK" or plrchoice == "1":
            if cpuchoice == 1:
                attack("enemy", plr["atk"])
            else:
                attack("enemy", (plr["atk"] - currentenemy["def"]))
                print(currentenemy["titles"], " defended! DMG DOWN")

        if cpuchoice == 1:
            attack("plr", currentenemy["atk"])
        else:
            changestat("enemy", "def", "percent", 200)

        if plr["hp"] <= 0:
            gameover()
        elif currentenemy["hp"] <= 0:

            print("You win!")
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
            else:
                print(oldlevel)
                print(level)
            break

if doTut.upper() == "Y":
    battle("Tutorial")