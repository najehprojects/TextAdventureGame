import math
import os
import sys
import time
import random
import copy

def wait(secs):
    time.sleep(secs/global_speed)

def clear():
    wait(1)
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

global_speed = 11
# I want to be able to up the speed for testing

story = {

    "info": {
        "lastSpeaker": "???",
        "lastScene": "I1",
    },

    "templates": {
        1: {
            "speaker": "???",
            "message": "test",
            "speed": 1,
            "type": 1,
            "next": "I2",
            "delay": 1,
        },

        2: {
            "speaker": "???",
            "message": "choose",
            "speed": 1,
            "type": 2,

            "options": ["A", "B"],
            "results": ["I3", "I4"],
            "delay": 1,
        },
    },

    "intro": {
        1: {
            "speaker": "???",
            "message": "Awaken now, hero!",
            "speed": 1.3,
            "type": 1,
            "next": "I2",
            "delay": 1,
        },

        2: {
            "speaker": "",
            "message": "As you open your eyes, warm light floods them softly.",
            "speed": 1.75,
            "type": 1,
            "next": "I3",
            "delay": 1,
        },

        3: {
            "speaker": "",
            "message": "The surroundings around you become clear, and a cathedral comes into view. A priest carrying the voice you heard stands close to where you are sat on the floor.",
            "speed": 1.75,
            "type": 1,
            "next": "I4",
            "delay": 1,
        },

        4: {
            "speaker": "",
            "message": "Many onlookers observe your every move, with tired yet hopeful faces.",
            "speed": 1.75,
            "type": 1,
            "next": "I5",
            "delay": 1,
        },

        5: {
            "speaker": "Mysterious Priest",
            "message": "You have been chosen to save our world!",
            "speed": 1.3,
            "type": 1,
            "next": "I6",
            "delay": 1,
        },

        6: {
            "speaker": "",
            "message": "You've been isekai'd! Chosen as a legendary hero!!",
            "speed": 2,
            "type": 1,
            "next": "I7",
            "delay": 1,
        },

        7: {
            "speaker": "",
            "message": "Your old life is no longer, and a life full of adventure, riches and fame awaits you as the hero of this world!",
            "speed": 1.75,
            "type": 1,
            "next": "I8",
            "delay": 1,
        },

        8: {
            "speaker": "Mysterious Priest",
            "message": "Brave hero, we require your immense strength to defeat the demon lord, Mr. Demon Lord!!!",
            "speed": 1.3,
            "type": 1,
            "next": "I9",
            "delay": 1,
        },

        9: {
            "speaker": "Mysterious Priest",
            "message": "First, we must require you to face some enemies to awaken your skills...",
            "speed": 1.3,
            "type": 1,
            "next": "I10",
            "delay": 1,
        },

        10: {
            "speaker": "",
            "message": "Something is off, and you feel like this might be a good time to escape...",
            "speed": 1,
            "type": 2,

            "options": ["Stay and face their training", "Try to flee"],
            "results": ["I96", "I11"],
            "delay": 1,
        },

        11: {
            "speaker": "",
            "message": "You scutter out of the cathedral, and suddenly the town outside peels away like a veil.",
            "speed": 1.3,
            "type": 1,
            "next": "I12",
            "delay": 1,
        },

        12: {
            "speaker": "",
            "message": "What remains are the ruins of a town, coated in thick a malicious purple mist.",
            "speed": 1.3,
            "type": 1,
            "next": "I13",
            "delay": 1,
        },

        13: {
            "speaker": "",
            "message": "It seems that leaving was the right option.",
            "speed": 1.3,
            "type": 1,
            "next": "I14",
            "delay": 1,
        },

        14: {
            "speaker": "",
            "message": "Suddenly, something emerges from the rubble of the cathedral you just escaped, it seems you aren't alone, and whatever was with you was strong enough to cast such a large illusion.",
            "speed": 1.3,
            "type": 1,
            "next": "I99",
            "delay": 1,
        },

        96: {
            "speaker": "",
            "message": "You stay sat down, and a malicious grins shines across the priest's face",
            "speed": 1.3,
            "type": 1,
            "next": "I97",
            "delay": 1,
        },

        97: {
            "speaker": "Mysterious Priest?",
            "message": "Courageous lord, consume the strength of this 'hero' and reinstate yourself as the emperor of this world!!",
            "speed": 1.3,
            "type": 1,
            "next": "I98",
            "delay": 1,
        },

        98: {
            "speaker": "Mysterious Priest?!",
            "message": "DEMON LORD: SUMMON!!!",
            "speed": 1.3,
            "type": 1,
            "next": "I99",
            "delay": 1,
        },

        99: {
            "speaker": "",
            "message": "",
            "speed": 1,
            "type": 1,
            "next": -1,
            "delay": 1,
        },

    },

    "worst": {

        1: {
            "speaker": "",
            "message": "It seems you got lucky that it's movements were slow enough to dodge",
            "speed": 1.3,
            "type": 1,
            "next": "W2",
            "delay": 1,
        },

        2: {
            "speaker": "???",
            "message": "Is it really dead?!",
            "speed": 1.6,
            "type": 1,
            "next": "W3",
            "delay": 1,
        },

        3: {
            "speaker": "",
            "message": "You turn around and spot a person crouched behind some rubble.",
            "speed": 1.3,
            "type": 1,
            "next": "W4",
            "delay": 1,
        },

        4: {
            "speaker": "",
            "message": "In fact, on further inspection, it seems that there are many people all around, hiding in the rubble all around.",
            "speed": 1.3,
            "type": 1,
            "next": "W5",
            "delay": 1,
        },

        5: {
            "speaker": "Random Old Man",
            "message": "Thank you! You're our hero!",
            "speed": 1.3,
            "type": 1,
            "next": "W6",
            "delay": 1,
        },

        6: {
            "speaker": "",
            "message": "As the thanks from the real but injured townspeople roar on, a few people lurk in the rubble still.",
            "speed": 1.3,
            "type": 1,
            "next": "W7",
            "delay": 1,
        },

        7: {
            "speaker": "",
            "message": "One girl with bright red hair very clearly poking from under her hood sits facing away from everyone.",
            "speed": 1,
            "type": 2,

            "options": ["Go over and talk to her", "Leave her be"],
            "results": ["O97", "W98"],
            "delay": 1,
        },

        10: {
            "speaker": "",
            "message": "2 MONTHS LATER",
            "speed": 0.7,
            "type": 1,
            "next": "W11",
            "delay": 3,
        },

        11: {
            "speaker": "",
            "message": "As the thanks from the real but injured townspeople roar on, a few people lurk in the rubble still.",
            "speed": 1.3,
            "type": 1,
            "next": "W7",
            "delay": 1,
        },

        98: {
            "speaker": "Random Citizen",
            "message": "Thank you so much for saving us!!",
            "speed": 1.3,
            "type": 1,
            "next": "I99",
            "delay": 1,
        },

        99: {
            "speaker": "",
            "message": "",
            "speed": 1.3,
            "type": 1,
            "next": -1,
            "delay": 1,
        },

    },

    "ok": {

            1: {
                "speaker": "",
                "message": "You approach the little girl, and as soon as you get close, a bright purple light erupts.",
                "speed": 1.3,
                "type": 1,
                "next": "O2",
                "delay": 1,
            },

            2: {
                "speaker": "Little Girl",
                "message": "STAY... STAY AWAY FROM ME!!",
                "speed": 1.3,
                "type": 1,
                "next": "O3",
                "delay": 1,
            },

            3: {
                "speaker": "",
                "message": "A bright pillar of light engulfs the surroundings",
                "speed": 1.3,
                "type": 1,
                "next": "O99",
                "delay": 1,
            },

            99: {
                "speaker": "",
                "message": "",
                "speed": 1.3,
                "type": 1,
                "next": -1,
                "delay": 1,
            },

        },
}

skillShop = {

    # Type 1 is damage set amount
    # Type 2 is damage set percentage

    # Type 3 is healing set amount
    # Type 4 is healing set percentage

    "skills": {

        1: {
            "spcost": 3,
            "name": "Low Heal",

            "type": 3,

            "manacost": 45,
            "amount": 10,

            "obtained": False,
        },

        2: {
            "spcost": 3,
            "name": "Slice",

            "type": 1,

            "manacost": 40,
            "amount": 30,

            "obtained": False,
        },

        3: {
            "spcost": 5,
            "name": "Heal",

            "type": 4,

            "manacost": 50,
            "amount": 15,

            "obtained": False,
        },

        4: {
            "spcost": 5,
            "name": "Slash",

            "type": 2,

            "manacost": 50,
            "amount": 20,

            "obtained": False,
        },

        5: {
            "spcost": 10,
            "name": "Master Heal",

            "type": 4,

            "manacost": 150,
            "amount": 50,

            "obtained": False,
        },

        6: {
            "spcost": 10,
            "name": "Execute",

            "type": 2,

            "manacost": 125,
            "amount": 65,

            "obtained": False,
        },

    },

}

plr = {
    "name": "",
    "weapon": "None",

    "inventory": [],

    "skills": [],

    "level": 66,
    "xp": 28710,

    "skillpoints": 3,

    "maxhp": 65,
    "maxmana": 100,

    "atk": 11,
    "def": 5,
    "hp": 65,

    "critChance": 12,
    "missChance": 5,

    "mana": 100,

    "title": " the Hero",

    "dif": "",

}

enemyTemplates = {

    "low": {
        "titles": ["Goblin", "Green Slime", "Skeleton", "Rotten Zombie", "Wolf"],
        "atk": 1,
        "def": 1,
        "hp": 12,
        "maxhp": 12,
        "critChance": 12,
        "missChance": 5,
        "xp": "low",
        "name": "",
        "battletext": "",
    },

    "mid": {
        "titles": ["Orc", "Blue Slime", "Armored Skeleton", "Zombie", "Wolf Pack Leader"],
        "atk": 7,
        "def": 5,
        "hp": 41,
        "maxhp": 41,
        "critChance": 12,
        "missChance": 5,
        "xp": "mid",
        "name": "",
        "battletext": "",
    },

    "shapeshifter": {
        "titles": ["The Shapeshifter"],
        "atk": 20,
        "def": 5,
        "hp": 150,
        "maxhp": 150,
        "critChance": 5,
        "missChance": 35,
        "xp": "mid",
        "name": "",
        "image": """
                    ██████                        
       █           ▓▒▒▒▒█▓█████         █▒▓█      
     █▓███     ████▓▓▒▓▓▒▓██▓▓▓█▓███████▒▓▓██     
     ▓█▓▒██  █▓▓▓█▓▓▓▓▒▓▓▓█▓▓▒▓██▓▓▓██▒▓▒█████    
      ▒▓▓██▓▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▒▒▓██▓█▓▒▓▓██▓▓██     
      █▓█▓▒▓██▓▓▓▒▒▓▓▒▒▓▒▒▓▓▓▒▓██▓▓████████▓▓█    
       █▓▒▓██▓▒▒▓▓▓█▓▓▓▓▒▒▓██▓█▓▓▒▓████████▒▓▓▒▓  
      █▓██▓██▓▓▓█▓▓██▓▓██▓▓█▓▓▓▓▒▒▓█████  █▓▓█▓██ 
   █▒▒▓▓█▓▓█▓▓▒▓▓▓█▓▓▓▓▓██▓▒▒▓▓▒▓▓▓█▓▓▓█▓█ ██▓████
   ███▓█▓▓██▓▓▓▒▒▓██▒▒▓▓▓▓▓▓▒▒▒▓▓▓▓███▓██████████ 
    █▓▒▒▓▓▓█▓▒▓▒▓█▓▓▒▒▓▓▓▓▓█▓▓▓▒▒▓█▓▓▓█▓█▓▓▓▓█    
  █▓▒▒▓▒▒▒▓▓▓▓▓▓███▓▓▓██████▓██▓▓▓███████▓▓▓▓██   
 █▓▒▓▒▒▒▓▒▓██▓█████▓▓███▒▓▒▒▒▓▓████████▓▓▓▓▒▓▓██  
 █▓▓▓▓▓▓▓▓▓███▓▓▓▓▓██▓▓▓▒▓▓▓▓▓▓▓█████▓█▓█▓▓▓▓▓▓█  
█▓▓▓▓▒▒▒▓█████▓▓▓▓▓▓▓▓▒▓███████▓▓▓▓▓▓▓██▓█▓▓▒▒▓██ 
█▓▓▓▓▓▓▓██▓▓██▓▒▒▒▒▓▓▓████▓▓▓▓▓▓▓▓▓▓▓██▓███▓▓▓▓██ 
█▓▓▓▓▓▓██▓██▓▓▓▓▓▓▓▓█▓██▓▓▓▓▓▓▓▒▒▓▓▓█▓█▓█▓▒▒▒▒███ 
 █▓█████████▓▓▓▓████████▓████▓▓▓▓▓██████▓▓█▓▓▓▓██ 
 ██▓▓▓▓███████████▓███▓▓▓▓█████████████████▓█▓▓██ 
█████████▓███▓▓▓▓▓▓▓▓▒▒▓▒▓▓▓███████▓▓▓██▓█████████
 █████████▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓█████ ████  
  ████████████████▓▓▓▓▓▓██▓████▓▓▓▓▓█▓██▓██       
    ████████████████████████████▓▓▓▓▓▓▓█▓▓▓█      
        ████████████████████████▓▓▓▓█▓████████    
       █████████████  ███████████▓█████████████   
     █████████████       ███████▓▓▓▓▓▓▓▓▓█        
       ███████████              ████████████      
        ████ ████                ██████████       
        """,
        "battletext": ["The air feels murky...", "It stares.", "It's limbs sluggishly and sloppily thrash around.", "A potent malicious presence radiates from it", "You can't quite tell what it is", "It smells like something died and then died again.", "It slowly expands and contracts, but it isn't breathing."],
    },

    "high": {
        "titles": ["Orc General", "Red Slime", "Skeleton Warrior", "Mutated Zombie", "Giant"],
        "atk": 15,
        "def": 7,
        "hp": 160,
        "maxhp": 160,
        "critChance": 10,
        "missChance": 7,
        "xp": "high",
        "name": "",
        "battletext": "",
    },

    "miniboss": {
        "titles": ["Fenrir", "Giant Black Slime", "Ancient Giant"],
        "atk": 24,
        "def": 12,
        "hp": 150,
        "maxhp": 150,
        "critChance": 12,
        "missChance": 5,
        "xp": "miniboss",
        "name": "",
        "battletext": "",
    },

    "finalboss": {
        "titles": ["The Demon Lord"],
        "atk": 50,
        "def": 50,
        "hp": 350,
        "maxhp": 350,
        "critChance": 12,
        "missChance": 1,
        "xp": "finalboss",
        "name": "",
        "battletext": ["You wonder why his name is so generic...", "Even through his face which is literally on flames, you can tell he's smiling.", "His precision is off the charts.", "You think of your days at home and wonder if being isekai'd was really a good thing."],
    },
}

def gameover(reason):
    clear()
    print("GAME OVER")

    if reason != "":
        animatetxt("You were killed by " + reason, 1)
    else:
        print()

    for i in range(1, 6):
        print("Closing game in " + str(6 - i) + "...")
        wait(1)

    exit(0)

def showstats():
    print()
    print("-<{[PLAYER STATS]}>-")
    print()
    print("[" + str.upper(plr["name"]) + str.upper(plr["title"]) + "]")
    print("Current Weapon:", plr["weapon"])
    print("Level:", plr["level"])
    print("XP:", plr["xp"])
    print()

def animatetxt(msg, spd):
    for chara in msg:
        sys.stdout.write(chara)
        sys.stdout.flush()

        if global_speed < 10:
            wait(0.1 / spd/ global_speed)

        if chara == ",":
            wait((0.5 / spd))

    print()

def storymanager(scenecode):
    scenecode = str(scenecode)

    scene_dir = ""
    scene_number = 0

    letter = scenecode[0]

    if letter == "I":
        scene_dir = "intro"
    if letter == "W":
        scene_dir = "worst"
    if letter == "B":
        scene_dir = "bad"
    if letter == "O":
        scene_dir = "ok"
    if letter == "G":
        scene_dir = "good"
    if letter == "P":
        scene_dir = "perfect"

    scene_number: int = int(scenecode[1:len(scenecode)])

    if story["info"]["lastSpeaker"] != story[scene_dir][scene_number]["speaker"]:
        print()

    if story[scene_dir][scene_number]["speaker"] != "":
        print(story[scene_dir][scene_number]["speaker"] + ": ", end="")

    story["info"]["lastSpeaker"] = story[scene_dir][scene_number]["speaker"]

    if story[scene_dir][scene_number]["type"] == 1 and story[scene_dir][scene_number]["next"] != -1:
        story["info"]["lastScene"] = scenecode

    if story[scene_dir][scene_number]["type"] == 1:

        animatetxt((story[scene_dir][scene_number]["message"]), (story[scene_dir][scene_number]["speed"]))

        if (story[scene_dir][scene_number]["next"]) != -1:
            wait(story[scene_dir][scene_number]["delay"])
            storymanager(str(story[scene_dir][scene_number]["next"]))

    elif story[scene_dir][scene_number]["type"] == 2:

        animatetxt((story[scene_dir][scene_number]["message"]), (story[scene_dir][scene_number]["speed"]))
        print()
        print("CHOOSE")
        options = story[scene_dir][scene_number]["options"]
        counter = 0
        for option in options:
            counter += 1
            print("[" + str(counter) + "]", option)

        choice = 0

        while not choice.is_integer() or not int(choice) <= counter or choice < 1:

            choice = input("Choice: ")

            try:
                choice = int(choice)
            except ValueError or choice < 1 or choice > counter or not choice.is_integer():
                print("Invalid choice")
                choice = 0

        storymanager(str(story[scene_dir][scene_number]["results"][choice - 1]))

animatetxt("Welcome to...", 1)
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
                                                                                                                                                 """,
           500)
wait(1)
input("Press enter to continue...")

clear()

print("First, please enter a name")
plr["name"] = input()

while plr["name"] == "":
    plr["name"] = input("Enter a valid name: ")

specialStory = False
skipSelection = False

if plr["name"].upper() == "ZERI":
    plr["maxhp"] = 99999999999999
    plr["hp"] = 99999999999999
    plr["dif"] = "NORMAL"

    plr["atk"] = 99999999999999
    plr["def"] = 101
    plr["level"] = 999
    plr["xp"] = 99999999999999
    plr["weapon"] = "Strong ahh stick"

    specialStory = True
    skipSelection = True

elif plr["name"].upper() == "CLOVII":
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
    skipSelection = True

elif plr["name"].upper() == "ENDLESSHERO":
    plr["dif"] = "NORMAL"
    plr["level"] = 0
    plr["xp"] = 0
    plr["nextxp"] = 100
    plr["skillpoints"] = 100
    plr["maxmana"] = 1000
    plr["mana"] = 1000

    specialStory = True
    skipSelection = True

    wait(3)

elif plr["name"].upper() == "UNDIES" or plr["name"].upper() == "PEACE":

    animatetxt("Wooden Stick Successfully enhanced to +99 reinforcement!!", 1)

    plr["weapon"] = "+99 Reinforced Wooden Stick"
    #plr["skills"] = ["Swing Up", "Swing Down", "Voracity"]
    plr["atk"] = 9999999
    plr["def"] = 700
    plr["maxhp"] = 9999
    plr["hp"] = 9999

    plr["dif"] = "NORMAL"

    skipSelection = True

    wait(3)

showstats()

def difficulty_select():
    print("Choose Your Difficulty")
    plr["dif"] = input("[Easy/Normal/Hard/Impossible] ")

    while plr["dif"].upper() != "EASY" and plr["dif"].upper() != "NORMAL" and plr["dif"].upper() != "HARD" and plr[
        "dif"].upper() != "IMPOSSIBLE" and plr["dif"].upper() != "E" and plr["dif"].upper() != "N" and plr[
        "dif"].upper() != "H" and plr["dif"].upper() != "I":
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
    print("Selected Difficulty " + plr["dif"])

if not skipSelection:
    difficulty_select()

    difCon = input("Are you sure you would like to proceed with difficulty " + plr["dif"] + "? " + "[Y/N]: ")
    while difCon.upper() != "Y":

        while difCon.upper() != "Y" and difCon.upper() != "N":
            difCon = input("Confirm difficulty " + plr["dif"] + "? " + "[Y/N]: ")

        if difCon.upper() == "N":
            difficulty_select()
            difCon = ""

    if plr["dif"] == "EASY":
        plr["maxhp"] += 25
        plr["hp"] += 25

        plr["atk"] += 10
        plr["def"] += 5

    elif plr["dif"] == "HARD":
        plr["maxhp"] -= 20
        plr["hp"] -= 20

    elif plr["dif"] == "IMPOSSIBLE":
        plr["maxhp"] -= 25
        plr["hp"] -= 25

def battle(enemy):
    clear()

    turn = 1

    def defence_calc(attacker_attack_stat, target_defence_stat):
        if target_defence_stat >= attacker_attack_stat:
            return attacker_attack_stat / 2
        else:
            return attacker_attack_stat * (1 - ((target_defence_stat / attacker_attack_stat) / 2))

    currentenemy = copy.deepcopy(enemyTemplates[enemy.lower()])
    currentenemy["name"] = enemyTemplates[enemy.lower()]["titles"][
        (random.randint(1, len(enemyTemplates[enemy.lower()]["titles"]))) - 1]

    while plr["hp"] > 0 and currentenemy["hp"] > 0:

        def activity(choice):

            cpuchoice = random.randint(1, 2)

            if choice == "ATK" or choice == "1":
                if cpuchoice == 1:
                    attack("enemy", plr["atk"], 0)
                    wait(1)
                    print()
                if cpuchoice == 2:
                    print(currentenemy["name"], "defended! DMG DOWN")
                    attack("enemy", math.ceil(defence_calc(plr["atk"], currentenemy["def"])), 0)
                    wait(1)
                    print()

            elif choice == "SKILL" or choice == "3":

                if len(plr["skills"]) > 0:
                    print("""
                    Choose Skill
                    [BACK] to exit
                    """)
                    count = 0
                    for skill in plr["skills"]:
                        count += 1
                        print(str(count) + ":", "SKILL NAME:", "<" + skill + ">")

                    chosenskill = input("Enter Skill Number/Name: ")

                    while chosenskill == "":
                        chosenskill = input("Enter Skill Number/Name: ")

                    chosenskill = chosenskill.upper()

                    if chosenskill == "BACK":
                        action()

                    if chosenskill.isdigit():
                        chosenskill = int(chosenskill)

                        if chosenskill > count or chosenskill <= 0:
                            print("Invalid Entry!!")
                            action()

                    for skillEntry in plr["skills"]:
                        current_skill = 0

                        if skillEntry.upper() == chosenskill or current_skill + 1 == chosenskill:
                            #print("SKILL FOUND!!", skillEntry)

                            current_skill += 1

                            for skill in skillShop["skills"]:

                                if skillShop["skills"][skill]["name"].upper() == skillEntry.upper():

                                    print()

                                    if plr["mana"] >= skillShop["skills"][skill]["manacost"]:
                                        plr["mana"] -= skillShop["skills"][skill]["manacost"]

                                        if skillShop["skills"][skill]["type"] == 1:
                                            attack("enemy", skillShop["skills"][skill]["amount"], 0)

                                        elif skillShop["skills"][skill]["type"] == 2:
                                            attack("enemy", skillShop["skills"][skill]["amount"], 1)

                                        elif skillShop["skills"][skill]["type"] == 3:
                                            plr["hp"] += math.ceil(skillShop["skills"][skill]["amount"])
                                            print("Healed", str(math.ceil(skillShop["skills"][skill]["amount"])) + " Health!")

                                        elif skillShop["skills"][skill]["type"] == 4:
                                            plr["hp"] += math.ceil(plr["maxhp"]*(skillShop["skills"][skill]["amount"]/100))
                                            if plr["hp"] > plr["maxhp"] and skillShop["skills"][skill]["name"].upper() != "MASTER HEAL":
                                                plr["hp"] = plr["maxhp"]
                                            print("Healed", str(math.ceil(plr["maxhp"]*(skillShop["skills"][skill]["amount"]/100))) + " Health!")

                                    else:
                                        print("NO MANA!")
                                        action()

                else:
                    print("No Skills!!")
                    action()

            elif choice == "UPGRADE" or choice == "6":
                print("""
                Choose Your Upgrade
                [BACK] to exit
                """)
                print("Skill Points:", plr["skillpoints"])
                for i in skillShop["skills"]:
                    if not skillShop["skills"][i]["obtained"]:
                        print(str(i) + ":", "SKILL NAME:", "<" + skillShop["skills"][i]["name"] + ">")
                        print("SP COST:", skillShop["skills"][i]["spcost"])

                chosenupgrade = input("Choose your Upgrade: ")

                while chosenupgrade == "":
                    chosenupgrade = input("Choose your Upgrade: ")

                chosenupgrade = chosenupgrade.upper()

                if chosenupgrade == "BACK":
                    action()

                bought = False

                if chosenupgrade.isdigit():
                    chosenupgrade = int(chosenupgrade)

                for skillEntry in skillShop["skills"]:
                    if skillShop["skills"][skillEntry]["name"].upper() == chosenupgrade or skillEntry == chosenupgrade:
                        if plr["skillpoints"] >= skillShop["skills"][skillEntry]["spcost"] and \
                                skillShop["skills"][skillEntry]["obtained"] == False:
                            print("BOUGHT SKILL", skillShop["skills"][skillEntry]["name"])
                            plr["skillpoints"] -= skillShop["skills"][skillEntry]["spcost"]
                            plr["skills"].append(skillShop["skills"][skillEntry]["name"])
                            skillShop["skills"][skillEntry]["obtained"] = True
                            bought = True
                            break
                        else:
                            if skillShop["skills"][skillEntry]["obtained"]:
                                print("You already have this skill!")
                            if plr["skillpoints"] < skillShop["skills"][skillEntry]["spcost"]:
                                print("Not enough points!")

                if not bought:
                    print("Upgrade unavailable")

                action()

            if currentenemy["hp"] >= 1:

                if cpuchoice == 1:
                    if choice == "DEF" or choice == "2":
                        print("You defended! DMG TAKEN DOWN")
                        attack("plr", math.ceil(defence_calc(currentenemy["atk"], plr["def"])), 0)
                        wait(1)
                        print()
                    else:
                        attack("plr", currentenemy["atk"], 0)
                        wait(1)
                        print()

            if choice == "2" and cpuchoice == 2 or choice == "DEF" and cpuchoice == 2:
                print("Both Parties Defended! No Damage was taken or dealt!")
                print()

        def action():

            nextaction = 0

            if nextaction != 0:
                nextaction = 0

            wait(3)
            clear()

            print(plr["name"], "VS.", currentenemy["name"] + "!")
            print()

            wait(1)

            print("{ TURN " + str(turn) + " }")
            if (plr["mana"] + 10) <= 100: plr["mana"] += 10
            print("Current Mana:", plr["mana"], "/", plr["maxmana"])
            print("Current HP:", plr["hp"], "/", plr["maxhp"])
            print()
            print("Enemy HP:", currentenemy["hp"], "/", currentenemy["maxhp"])

            if currentenemy["battletext"] != "":
                print()
                print(currentenemy["battletext"][random.randint(1,len(currentenemy["battletext"]))-1])

            print()
            nextaction = input(
                "Choose your action [ ATK - 1 / DEF - 2 / SKILL - 3 / ITEM - 4 / RUN - 5 / UPGRADE - 6 ]: ")
            print()
            while nextaction.upper() != "ATK" and nextaction.upper() != "DEF" and nextaction.upper() != "SKILL" and nextaction.upper() != "ITEM" and nextaction.upper() != "RUN" and nextaction.upper() != "UPGRADE" and nextaction != "1" and nextaction != "2" and nextaction != "3" and nextaction != "4" and nextaction != "5" and nextaction != "6":
                nextaction = input(
                    "Choose your action [ ATK - 1 / DEF - 2 / SKILL - 3 / ITEM - 4 / RUN - 5 / UPGRADE - 6 ]: ")
                print()

            activity(nextaction)

        def attack(target, damage, skilla):

            chance = random.randint(1, 100)

            crit_chance = 0
            miss_chance = 0

            if target == "plr":
                crit_chance = currentenemy["critChance"]
                miss_chance = currentenemy["missChance"]
            elif target == "enemy":
                crit_chance = plr["critChance"]
                miss_chance = plr["missChance"]

            if chance <= crit_chance:
                damage = damage * (random.randint(2, 3))
                print("Critical attack!")

            if chance >= (100 - miss_chance):
                damage = 0
                print("Miss!")

            if skilla == 0:
                if target == "plr":
                    plr["hp"] -= math.ceil(damage)
                    print("You took", math.ceil(damage), "damage!")
                    if plr["hp"] < 0: plr["hp"] = 0
                    print("You have", plr["hp"], "HP left!")
                    print()
                if target == "enemy":
                    currentenemy["hp"] -= math.ceil(damage)
                    print("You dealt", math.ceil(damage), "damage!")
                    if currentenemy["hp"] < 0: currentenemy["hp"] = 0
                    print(currentenemy["name"], "has", currentenemy["hp"], "HP left!")
                    print()

            if skilla == 1:
                if target == "enemy":
                    currentenemy["hp"] -= math.ceil(currentenemy["maxhp"]*(damage/100))
                    print("You dealt", math.ceil(currentenemy["maxhp"]*(damage/100)), "damage!")
                    if currentenemy["hp"] < 0: currentenemy["hp"] = 0
                    print(currentenemy["name"], "has", currentenemy["hp"], "HP left!")
                    print()

        action()

        if plr["hp"] <= 0:
            gameover(currentenemy["name"])
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
                while totalxp >= 100 + (10 * levels):
                    totalxp -= 100 + (10 * levels)
                    levels += 1
                    # print("Current Level:", levels, "XP Left:", totalxp)
                plr["level"] = levels
                return totalxp

            if oldlevel < 999:

                plr["nextxp"] = (100 + (10 * plr["level"]) - levelandxp(plr["xp"], 0))

                if plr["level"] == oldlevel:
                    print("XP till next level:", plr["nextxp"])

                if plr["level"] > oldlevel:
                    print("LEVEL UP!")
                    print("<" + str(oldlevel) + ">", "-->", "<" + str(plr["level"]) + ">")

                    plr["maxhp"] += (2 * (plr["level"] - oldlevel))
                    plr["maxmana"] += (3 * (plr["level"] - oldlevel))
                    plr["atk"] += (2 * (plr["level"] - oldlevel))

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

clear()

wait(1)

if not specialStory:

    storymanager("I1")

    if story["info"]["lastScene"] == "I98":

        clear()

        animatetxt("An ominous aura spreads across the cathedral...", 0.8)
        animatetxt("It seems the final battle is starting already", 0.6)

        enemyTemplates["finalboss"]["maxhp"] = 500
        enemyTemplates["finalboss"]["hp"] = 500
        enemyTemplates["finalboss"]["atk"] = 100
        enemyTemplates["finalboss"]["def"] = 99
        enemyTemplates["finalboss"]["battletext"] = ["You wonder why his name is so generic...", "He looks bored.", "He's probably holding back.", "You're cooked.", "There's no way out of this one.", "You're done.", "You probably should've ran when you had the chance.", "You feel somewhat weak."]
        battle("Finalboss")
        animatetxt("You did it... somehow?", 1)
        animatetxt("What to do now?", 1)
        clear()
        print("""MYSTERY ENDING?
        Beating this wasn't supposed to be possible, so you deserve a round of applause.""")
        gameover("")
    else:
        print(enemyTemplates["shapeshifter"]["image"])
        animatetxt("The... thing, it moves into your path", 0.3)
        wait(2)
        animatetxt("You have no other choice", 0.3)
        battle("Shapeshifter")
        storymanager("W1")

    clear()

    if story["info"]["lastScene"] == "W98":
        storymanager("W10")
        print("<End of story>")
    else:
        #storymanager("O1")
        print("<End of story>")

elif plr["name"].upper() == "CLOVII":
    animatetxt("Just because I added a story to the base game doesn't mean that you get to do whatever you want now!",
               2)
    wait(3)

    while plr["level"] < 999:
        newEn = random.randint(1, 3)
        if newEn == 1:
            battle("Mid")
        elif newEn == 2:
            battle("High")
        elif newEn == 3:
            battle("Miniboss")

    battle("Finalboss")

elif plr["name"].upper() == "ENDLESSHERO":
    while plr["level"] < 999:
        newEn = random.randint(1, 4)
        if newEn == 1:
            battle("Low")
        elif newEn == 2:
            battle("Mid")
        elif newEn == 3:
            battle("High")
        elif newEn == 4:
            battle("Miniboss")
