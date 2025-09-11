import sys
import time
import random
import os

def wait(secs):
   time.sleep(secs)

plr = {
    "name" : "",
    "pos" : 0,
    "items" : [""],
    "weapon" : "None",
    "scene" : "Intro",
    "level" : 1,
    "xp" : 0,
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

doTut = input("Would you like to play the tutorial? [Y/N]: ")

while doTut.upper() != "Y" and doTut.upper() != "N":
    doTut = input("Would you like to play the tutorial? [Y/N]: ")