import pickle
import os

import random
import time
import settings

filename = settings.SaveDirectory + settings.GoalManagerFileName
goal_array = []
rand10_array = []

# Objects to be stored in the file
class Goal:
    def __init__(self, name, status):
        self.status = status
        self.name = name


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
    print("- "*20)
    print(goal_array[int(index)].name, "is deleted!")
    time.sleep(1)
    goal_array.pop(int(index))

def randmode():
    rand10_array.clear()
    for x in range(10):
        rand = random.randint(0, len(goal_array)-1)
        rand10_array.append(rand)

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

    com = input("Enter a command: ")
    match com:
        case "load":
            goal_array = load(filename)
        case "save":
            save(filename, goal_array)

        case "add":
            inp = input("Enter a name: ")
            goal = Goal(inp, "ongoing")
            add(goal)

        case "remove":
            inp = input("Index to remove: ")
            remove(inp)
        
        case "help":
            print("help, load, save, add, remove, exit, invert, randm, defm")

        case "invert":
            goal_array = goal_array[::-1]

        case "randm":
            defmode = False
            rand10mode = True

        case "defm":
            defmode = True
            rand10mode = False

        case "exit":
            quit()

    
