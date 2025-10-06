import math
import os
import sys
import time
import random
import copy

def wait(secs):
   time.sleep(secs)

def clear():
    wait(1)
    #print('Clear')
    os.system("cls")

# type 1 is character speech / narration
# type 2 is a decision

# I[] is intro

# W[] is Worst Ending route (default)
# B[] is Bad Ending route
# O[] is Ok Ending route
# G[] is Good Ending route
# P[] is Perfect Ending route
# S[] is Secret Ending


story = {

    "templates" : {
        1: {
            "message": "test",
            "speed": 1,
            "type": 1,
            "next": "I2",
            "events": [""],
        },

        2: {
            "message": "choose",
            "speed": 1,
            "type": 2,

            "options": ["A", "B"],
            "results": ["I3", "I4"],
            "events": [""],
        },
    },

    "intro" : {
        1 : {
            "message" : "???: Awaken now, hero!",
            "speed" : 1.3,
            "type" : 1,
            "next" : "I2",
            "events": "",
            "delay" : 1,
        },

        2 : {
            "message" : "As you open your eyes, soft warm light fills them.",
            "speed" : 1.75,
            "type" : 1,
            "next" : "I3",
            "events": "",
            "delay" : 1,
        },

        3: {
            "message": "The surroundings around you become clear, and a cathedral comes into view. Many onlookers observe your every move, with tired yet hopeful faces",
            "speed": 1.75,
            "type": 1,
            "next": "I4",
            "events": "",
            "delay" : 1,
        },

        4: {
            "message": "???: You have been chosen to save our world!",
            "speed": 1.3,
            "type": 1,
            "next": "I5",
            "events": "",
            "delay" : 1,
        },

        5: {
            "message": "You've been isekai'd! Chosen as a legendary hero!!",
            "speed": 2,
            "type": 1,
            "next": "I6",
            "events": "",
            "delay" : 1,
        },

        6: {
            "message": "Your old life is no longer, and a life full of adventure, riches and fame awaits you as the hero of this world!",
            "speed": 1.75,
            "type": 1,
            "next": "I99",
            "events": "",
            "delay" : 1,
        },

        99: {
            "message": "test",
            "speed": 1,
            "type": 1,
            "next": -1,
            "events": "",
            "delay" : 1,
        },

    }
}

skillShop = {

    "skills" : {

        1 : {
            "spcost" : 3,
            "name": "Low Heal",
            "manacost": 45,

            "healamount": 10,
            "obtained" : False,
        },

        2 : {
            "spcost" : 3,
            "name": "Slow",
            "manacost": 35,

            "debufftype" : "atk",
            "debuffamount": 5,
            "debuffduration" : 2,
            "obtained" : False,
        },

        3 : {
            "spcost" : 3,
            "name": "Slice",
            "manacost": 40,

            "damage" : 25,
            "obtained" : False,
        },

        4 : {
            "spcost": 5,
            "name" : "Heal",
            "manacost": 50,

            "healpercentage": 25,
            "obtained" : False,
        },

        5 : {
            "spcost": 5,
            "name" : "Poison",
            "manacost": 50,

            "poisondamage": 5,
            "debufftype": "def",
            "debuffamount": 5,
            "debuffduration" : 5,
            "obtained" : False,
        },

        6 : {
            "spcost": 5,
            "name" : "Slash",
            "manacost": 50,

            "damage" : 35,
            "obtained" : False,
        },

        7 : {
            "spcost": 10,

            "name": "Master Heal",
            "manacost": 75,

            "healpercentage": 50,
            "obtained" : False,
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
            "obtained" : False,
        },

        9 : {
            "spcost": 10,

            "name": "Execute",
            "manacost": 75,

            "damage" : 65,
            "obtained" : False,
        },

    },

}

plr = {
    "name" : "",
    "weapon" : "None",

    "inventory": [""],

    "skills" : [""],

    "level" : 66,
    "xp" : 28710,

    "skillpoints" : 3,

    "maxhp" : 100,
    "maxmana" : 100,

    "atk" : 20,
    "def" : 10,
    "hp" : 110,

    "critChance": 12,
    "missChance": 5,

    "mana" : 100,

    "title" : " the Hero",

    "scene": "Intro",
    "moves" : 5,
    "pos": 0,

    "dif" : "",

}

enemyTemplates = {

    "tutorial" : {
        "titles" : ["Training Dummy"],
        "atk" : 1,
        "def" : 0,
        "hp" : 100,
        "critChance": 12,
        "missChance": 5,
        "xp" : "tutorial",
        "name" : "",
        "battletext" : [""],
    },

    "low" : {
        "titles" : ["Goblin", "Green Slime", "Skeleton", "Rotten Zombie", "Wolf"],
        "atk": 1,
        "def": 1,
        "hp": 6,
        "critChance": 12,
        "missChance": 5,
        "xp" : "low",
        "name" : "",
        "battletext" : [""],
    },

    "mid" : {
        "titles" : ["Orc", "Blue Slime", "Armored Skeleton", "Zombie", "Wolf Pack Leader"],
        "atk": 7,
        "def": 5,
        "hp": 41,
        "critChance": 12,
        "missChance": 5,
        "xp" : "mid",
        "name" : "",
        "battletext" : [""],
    },

    "high": {
        "titles" : ["Orc General", "Red Slime", "Skeleton Warrior", "Mutated Zombie", "Giant"],
        "atk": 15,
        "def": 7,
        "hp": 85,
        "critChance": 12,
        "missChance": 5,
        "xp" : "high",
        "name" : "",
        "battletext" : [""],
    },

    "miniboss": {
        "titles" : ["Fenrir", "Giant Black Slime", "Ancient Giant"],
        "atk": 24,
        "def": 12,
        "hp": 150,
        "critChance": 12,
        "missChance": 5,
        "xp" : "miniboss",
        "name" : "",
        "battletext" : [""],
    },

    "finalboss": {
        "titles" : ["The Dark Lord"],
        "atk": 50,
        "def": 50,
        "hp": 350,
        "critChance": 12,
        "missChance": 5,
        "xp" : "finalboss",
        "name" : "",
        "battletext" : [""],
    },
}

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
        wait(0.1/spd)
        if chara == ",":
            wait((0.5/spd))

    print()

def storymanager(scenecode):

    def event(newevent):
        print(newevent)

    scenecode = str(scenecode)

    sceneDIR = ""
    sceneNUMBER = 0

    letter = scenecode[0]

    if letter == "I":
        sceneDIR = "intro"
    elif letter == "W":
        sceneDIR = "worst"
    elif letter == "B":
        sceneDIR = "bad"
    elif letter == "O":
        sceneDIR = "ok"
    elif letter == "G":
        sceneDIR = "good"
    elif letter == "P":
        sceneDIR = "perfect"

    sceneNUMBER = int(scenecode[1:len(scenecode)])
    #print("Scene directory:", sceneDIR)
    #print("Scene number:", sceneNUMBER)

    if story[sceneDIR][sceneNUMBER]["type"] == 1:

        animatetxt((story[sceneDIR][sceneNUMBER]["message"]), (story[sceneDIR][sceneNUMBER]["speed"]))

        if story[sceneDIR][sceneNUMBER]["events"] != "":
            print(story[sceneDIR][sceneNUMBER]["events"])
            print("EVENT DETECTED")

        if (story[sceneDIR][sceneNUMBER]["next"]) != -1:
            wait(story[sceneDIR][sceneNUMBER]["delay"])
            storymanager(str(story[sceneDIR][sceneNUMBER]["next"]))

    elif story[sceneDIR][sceneNUMBER]["type"] == 2:

        animatetxt((story[sceneDIR][sceneNUMBER]["message"]), (story[sceneDIR][sceneNUMBER]["speed"]))
        print("CHOOSE")
        options = story[sceneDIR][sceneNUMBER]["options"]
        counter = 0
        for option in options:
            counter += 1
            print("["+str(counter)+"]", option)

        choice = int(input("Choice: "))

        while not choice <= counter or choice < 1:
            choice = int(input("Choice: "))

        storymanager(str(story[sceneDIR][sceneNUMBER]["results"][choice-1]))

animatetxt("Welcome to...",1)
print()
animatetxt("""
 .d8888b.  888                                                  8888888     888 d8b          888         888    888                          888 
d88P  Y88b 888                                                    888       888 Y8P          888         888    888                          888 
888    888 888                                                    888       888              888         888    888                          888 
888        88888b.   .d88b.   .d88b.  .d8888b   .d88b.            888   .d88888 888  .d88b.  888888      8888888888  .d88b.  888d888 .d88b.  888 
888        888 "88b d88""88b d88""88b 88K      d8P  Y8b           888  d88" 888 888 d88""88b 888         888    888 d8P  Y8b 888P"  d88""88b 888 
888    888 888  888 888  888 888  888 "Y8888b. 88888888           888  888  888 888 888  888 888         888    888 88888888 888    888  888 Y8P 
Y88b  d88P 888  888 Y88..88P Y88..88P      X88 Y8b.    d8b        888  Y88b 888 888 Y88..88P Y88b.       888    888 Y8b.     888    Y88..88P  "  
 "Y8888P"  888  888  "Y88P"   "Y88P"   88888P'  "Y8888 88P      8888888 "Y88888 888  "Y88P"   "Y888      888    888  "Y8888  888     "Y88P"  888 
                                                       8P                                                                                        
                                                       "                                                                                         
                                                                                                                                                 """, 500)
wait(1)
input("Press enter to continue...")

clear()

print("First, please enter a name")
plr["name"] = input()

while plr["name"] == "":
    plr["name"] = input("Enter a valid name: ")

specialStory = False

if plr["name"] == "Zeri":
    plr["maxhp"] = 99999999999999
    plr["hp"] = 99999999999999
    plr["dif"] = "NORMAL"

    plr["atk"] = 99999999999999
    plr["def"] = 101
    plr["level"] = 999
    plr["xp"] = 99999999999999
    plr["weapon"] = "Strong ahh stick"

    specialStory = True
elif plr["name"] == "Hero":
    animatetxt("So you've chosen this path...", 0.9)
    plr["hp"] = 2
    plr["maxhp"] = 2
    plr["atk"] = 701
    plr["def"] = 99
    plr["dif"] = "NORMAL"
    plr["title"] = ", the True Saviour"
    plr["level"] = 999
    plr["xp"] = 99999999999999
    plr["weapon"] = "The Legendary Blade, Excalibur"

    enemyTemplates["finalboss"]["atk"] = 75

    specialStory = True
elif plr["name"] == "Clovii":
    animatetxt("Goodluck... :)", 0.9)
    plr["hp"] = 5
    plr["maxhp"] = 5
    plr["atk"] = 100
    plr["def"] = 99
    plr["dif"] = "NORMAL"
    plr["title"] = ", the Bullied One"
    plr["level"] = 995
    plr["xp"] = 5000000
    plr["nextxp"] = 10000
    plr["weapon"] = "A Branch"

    enemyTemplates["finalboss"]["atk"] = 9999999
    enemyTemplates["finalboss"]["def"] = 200
    enemyTemplates["finalboss"]["hp"] = 999
    enemyTemplates["finalboss"]["titles"] = ["Full Power Zeri"]

    specialStory = True
elif plr["name"] == "Test":
    plr["dif"] = "NORMAL"
    plr["level"] = 0
    plr["xp"] = 0
    plr["nextxp"] = 100

    specialStory = True

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

if not specialStory:
    difficulty_select()

    difCon = input("Are you sure you would like to proceed with difficulty "+ plr["dif"]+"? "+ "[Y/N]: ")
    while difCon.upper() != "Y":

        while difCon.upper() != "Y" and difCon.upper() != "N":
            difCon = input("Confirm difficulty "+ plr["dif"]+"? "+ "[Y/N]: ")

        if difCon.upper() == "N":
            difficulty_select()
            difCon = ""

    if plr["dif"] == "EASY":
        plr["maxhp"] += 25
        plr["hp"] += 25

        plr["atk"] += 10
        plr["def"] += 5

    elif plr["dif"] == "HARD":
        plr["maxhp"] -= 25
        plr["hp"] -= 25

    elif plr["dif"] == "IMPOSSIBLE":
        plr["maxhp"] -= 25
        plr["hp"] -= 25

doTut = input("Would you like to play the tutorial? [Y/N]: ")
while doTut.upper() != "Y" and doTut.upper() != "N":
    doTut = input("Would you like to play the tutorial? [Y/N]: ")

tutorialComplete = False

def battle(enemy):

    clear()

    turn = 1

    currentenemy = copy.deepcopy(enemyTemplates[enemy.lower()])
    currentenemy["name"] = enemyTemplates[enemy.lower()]["titles"][(random.randint(1, len(enemyTemplates[enemy.lower()]["titles"]))) - 1]

    if enemy.lower() == "tutorial":
        while not tutorialComplete:
            print("Welcome to the Tutorial!")
            break

    while plr["hp"] > 0 and currentenemy["hp"] > 0:

        def action():

            wait(3)
            clear()

            print(plr["name"], "VS.", currentenemy["name"] + "!")
            print()

            wait(1)

            print("{ TURN " + str(turn) + " }")
            if (plr["mana"] + 10) <= 100: plr["mana"] += 10
            print("Current Mana:", plr["mana"], "/", plr["maxmana"])
            print("Current HP:", plr["hp"], "/", plr["maxhp"])
            nextaction = input("Choose your action [ATK - 1 / DEF - 2 / SKILL - 3 / ITEM - 4 / RUN - 5 / UPGRADE - 6 ]: ")
            print()
            while nextaction.upper() != "ATK" and nextaction.upper() != "DEF" and nextaction.upper() != "SKILL" and nextaction.upper() != "ITEM" and nextaction.upper() != "RUN" and nextaction.upper() != "UPGRADE" and nextaction != "1" and nextaction != "2" and nextaction != "3" and nextaction != "4" and nextaction != "5" and nextaction != "6":
                nextaction = input("Choose your action [ATK - 1 / DEF - 2 / SKILL - 3 / ITEM - 4 / RUN - 5 / UPGRADE - 6 ]: ")
                print()
            return nextaction

        def attack(target, damage, skilla):

            chance = random.randint(1,100)

            critChance = 0
            missChance = 0

            if target == "plr":
                critChance = currentenemy["critChance"]
            elif target == "enemy":
                critChance = plr["critChance"]

            if target == "plr":
                critChance = currentenemy["missChance"]
            elif target == "enemy":
                critChance = plr["missChance"]

            if chance <= critChance:
                damage = damage*(random.randint(2,3))
                print("Critical attack!")

            if chance >= (100-missChance):
                damage = 0
                print("Miss!")

            if skilla == 0:
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
            if skilla == 1:
                print("a")

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

        elif plrchoice == "SKILL" or plrchoice == "3":
            print()
            print("Choose Your Skill")
            for skill in plr["skills"]:
                print(skill)

        elif plrchoice == "UPGRADE" or plrchoice == "6":
            print()
            print("Choose Your Upgrade")
            print("Skill Points:", plr["skillpoints"])
            for i in skillShop["skills"]:
                if not skillShop["skills"][i]["obtained"]:
                    print(str(i)+":","SKILL NAME:", "<"+skillShop["skills"][i]["name"]+">")
                    print("SP COST:", skillShop["skills"][i]["spcost"])

            chosenupgrade = input("Choose your Upgrade: ")

            for _ in skillShop["skills"]:

                if skillShop["skills"][_]["name"] == chosenupgrade and plr["skillpoints"] >= skillShop["skills"][_]["spcost"] and skillShop["skills"][_]["obtained"] == False:
                    print("BOUGHT SKILL", skillShop["skills"][_]["name"])
                    plr["skillpoints"] -= skillShop["skills"][_]["spcost"]
                    plr["skills"].append(skillShop["skills"][_]["name"])
                    skillShop["skills"][_]["obtained"] = True

                else:
                    while True:
                        for _ in skillShop["skills"]:
                            if skillShop["skills"][_]["name"] == chosenupgrade and plr["skillpoints"] >= skillShop["skills"][_]["spcost"] and skillShop["skills"][_]["obtained"] == False:
                                break
                        chosenupgrade = input("Invalid Option, Choose your Upgrade: ")

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

            plr["xp"] += xpgain
            oldlevel = plr["level"]

            def levelandxp(totalxp, levels):
                while totalxp >= 100+(10*levels):
                    totalxp -= 100+(10*levels)
                    levels += 1
                    #print("Current Level:", levels, "XP Left:", totalxp)
                plr["level"] = levels
                return totalxp

            if oldlevel < 999:

                plr["nextxp"] = (100+(10*plr["level"]) - levelandxp(plr["xp"], 0))

                if plr["level"] == oldlevel:
                    print("XP till next level:", plr["nextxp"])

                if plr["level"] > oldlevel:
                    print("LEVEL UP!")
                    print("<"+str(oldlevel)+">", "-->", "<"+str(plr["level"])+">")

                    plr["maxhp"] += (10 * (plr["level"] - oldlevel))
                    plr["maxmana"] += (10 * (plr["level"] - oldlevel))
                    plr["atk"] += (5 * (plr["level"] - oldlevel))

                    if plr["def"] + (plr["level"] - oldlevel) <= 99:
                        plr["def"] += (plr["level"] - oldlevel)
                    else:
                        print("Defence MAXED!")

                    plr["skillpoints"] += (plr["level"] - oldlevel)
                    plr["hp"] = plr["maxhp"]
                    plr["mana"] = plr["maxmana"]
                    print()
                    showstats()
                    wait(3)
                break
            else:
                print("Level MAX!")

            print()

            wait(2)

        turn += 1

#print("Battle System Tests")

if doTut.upper() == "Y":
    print("Proper Tutorial not yet implemented")
    #battle("Tutorial")

wait(1)

clear()

wait(1)

if not specialStory:

    storymanager("I1")

    animatetxt("ABCDEF BATTLE TEST", 1)

    battle("Low")
    battle("Mid")
    battle("High")
    battle("Miniboss")
    battle("Low")
    battle("Finalboss")

elif plr["name"] == "Clovii":
    animatetxt("Just because I added a story to the base game doesn't mean that you get to do whatever you want now!", 2)
    wait(3)

    while plr["level"] < 999:
        newEn = random.randint(1,3)
        if newEn == 1:
            battle("Mid")
        elif newEn == 2:
            battle("High")
        elif newEn == 3:
            battle("Miniboss")

    battle("Finalboss")