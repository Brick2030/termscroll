import pickle
import os

import random
import time
import settings

filename = settings.SaveDirectory + settings.GoalManagerFileName
goal_array = []
rand10_array = []
status_msg = "Welcome to termscroll!"

# Objects to be stored in the file
class Goal:
    def __init__(self, name, status):
        self.status = status
        self.name = name

# Functions ----------------------------------------------------------------------------------

def save(filename, goals): # goals are array
    with open(filename, "wb") as f:
        pickle.dump(goals, f)

def load(filename):
    with open(filename, "rb") as f:
        loaded_goals = pickle.load(f)
    return loaded_goals # return array

def add(goal):
    goal_array.append(goal)

def remove(index):
    goal_array.pop(int(index))

def randmode():
    rand10_array.clear()
    for x in range(10):
        rand = random.randint(0, len(goal_array)-1)
        rand10_array.append(rand)

def ShowStatus(msg):
    global status_msg
    status_msg = "Status: " + msg

# Core -----------------------------------------------------------------------

defmode = True
rand10mode = False

while(True):
    
    os.system('cls' if os.name == 'nt' else 'clear')

    if (defmode):
        for x, i in enumerate(goal_array):
            if (i.status == "ongoing"): 
                print(f"%d  %s" % (x, i.name))

    if (rand10mode):
        randmode()
        for x, i in enumerate(goal_array):
            if (i.status == "ongoing" and rand10_array.count(x) > 0): 
                print(f"%d  %s \n" % (x, i.name))

    # Status message
    print("- - - "*20, f"\n{status_msg}")






# Controls ---------------------------------------------------------------------
    com = input("Enter a command: ")
    match com:
        case "load":
            goal_array = load(filename)
            ShowStatus(f"{filename} was loaded...")

        case "save":
            save(filename, goal_array)
            ShowStatus(f"{filename} was saved...")

        case "add":
            inp = input("Enter a name: ")
            goal = Goal(inp, "ongoing")
            add(goal)
            ShowStatus(f"{goal} was added...")

        case "remove":
            inp = input("Index to remove: ")
            remove(inp)
            ShowStatus(f"{goal_array[int(inp)].name} was removed...")
        
        case "help":
            ShowStatus("help, load, save, add, remove, exit, invert, randm, defm")

        case "invert":
            goal_array = goal_array[::-1]
            ShowStatus("Array was inverted.")

        case "randm":
            defmode = False
            rand10mode = True

        case "defm":
            defmode = True
            rand10mode = False

        case "exit":
            ShowStatus("Dont leave! ToT") 
            quit()

    
