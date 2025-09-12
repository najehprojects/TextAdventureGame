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
    "atk" : 1,
    "def" : 1,
    "hp" : 10,

    "scene": "Intro",
    "moves" : 50,
    "pos": 0,

    "dif" : ""
}

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
    print(plr["name"], "VS.", enemy)