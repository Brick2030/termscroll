import pickle
import os

# Simple app for converting from GMstorage default file to txt file. Just exports.
# Will be deleted later.

class Goal:
    def __init__(self, name, status):
        self.status = status
        self.name = name

def load(filename):
    with open(filename, "rb") as f:
        loaded_goals = pickle.load(f)
    return loaded_goals # return array

output = ""

goals = load("./storage/GMstorage")
for oneGoal in goals:
    output = output + oneGoal.name + "\n" + "\n"

#print(output)

f = open("export.txt", "w")
f.write(output)
f.close()