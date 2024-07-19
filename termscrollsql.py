import sqlite3
import settings
import os
import time
import random

DateToday = time.strftime(settings.DateLayout)
FileName = settings.SaveDirectory + settings.FileName
status_msg = "Welcome to termscroll! Type \"h\" to see all commands!"

random_output_max : int = 5
_random_output : bool = False # Bool var for randomized output. 
_find_results_output : bool = False # Bool for results of search
_search_results = [] # Search result array. Used by function.
_search_word : str = "Hello" # Find function global input.
# Making a database:
with sqlite3.connect(FileName) as DataBase:
    pass
crs = DataBase.cursor()

# Making a "goals" table:
crs.execute("""CREATE TABLE IF NOT EXISTS goals(
     _goalText text,
     _dateWhenCreated text,
     _dateWhenLastInteracted text
     )""")

# Functions: -------------------------------------------------------------------------
def ShowDB_Default():

    if(_find_results_output):
        crs.execute("SELECT rowid, * FROM goals") # Find results output
        all_tasks = crs.fetchall()
        task_string : str = ""
        start_index : int = 0
        _search_results.clear()
        for task in all_tasks:
            if _search_word.lower() in task[1].lower(): _search_results.append(f"[{task[0]}]: {task[1]}")


        if (len(_search_results) == 0):
            print("No matches found.")
        else: 
            for i in _search_results:
                print(i)





    if(_random_output and not _find_results_output): # Random output
        crs.execute("SELECT rowid, * FROM goals")
        all_tasks = crs.fetchall()
        rand_queue = []
        for i in range(random_output_max):
            rand_temp : int = random.randint(0, len(all_tasks)-1)
            if (rand_queue.count(rand_temp) == 0): rand_queue.append(rand_temp)
        for i in rand_queue: 
            print(f"[{i+1}]: {all_tasks[i][1]}")

    elif(not _random_output and not _find_results_output): # Default output
        crs.execute("SELECT rowid, * FROM goals")
        items = crs.fetchall()
        for i in items:
            print(f"[{i[0]}]: {i[1]}")
        print(len(items)) ##############
    


def ShowStatus(msg):
    global status_msg
    status_msg = "Status: " + msg

def Add(GoalText):
    createDate = DateToday
    watchedDate = ''
    crs.execute(f"INSERT INTO goals VALUES ('{GoalText}', '{createDate}','{watchedDate}')")

# def watch - will be called to changed watched date. 
def Save():
    DataBase.commit()

def Load():
    with sqlite3.connect(FileName) as DataBase:
        pass

def Remove(inp): # It's called by status show and returns status... sorry...
    crs.execute(f"SELECT rowid, * FROM goals WHERE rowid = {inp}")
    removed = crs.fetchall()
    inp2 = input(f"You really want to remove {removed[0][1]}?\ny/n: ")
    if(inp2 == "y"): 
        crs.execute(f"DELETE FROM goals WHERE rowid = {inp}")
        return (f"{removed[0][1]} was removed.")
    else: return "canceled"

def Edit(inp):
    crs.execute(f"SELECT rowid, * FROM goals WHERE rowid = {inp}")
    toedit = crs.fetchall()
    inp2 = input("Enter edited goal text: ")
    crs.execute(f"UPDATE goals SET _goalText = '{inp2}' WHERE rowid = {inp}")
    return toedit[0][1]

# Core: --------------------------------------------------------------------------------
while(True):
    os.system('cls' if os.name == 'nt' else 'clear')
    ShowDB_Default()
    print("- - - " * 20, f"\n{status_msg}") # instead of 20 use term widtch.
# Controls: ----------------------------------------------------------------------------
    com = input("Enter a command: ")
    match com:

        case "a":
            inp = input("Enter a name: ")
            Add(inp)
            ShowStatus(f"{inp} < was added...")

        case "s":
            Save()
            ShowStatus("File was saved.")

        case "l":
            Load()
            ShowStatus("This feature doesnt work sorry.")

        case "r":
            inp = input("Enter ID to remove: ")
            ShowStatus(f"{Remove(inp)}")

        case "e":
            inp = input("Enter ID to edit: ")
            ShowStatus(f"[{inp}]: > {Edit(inp)} < was changed.")

        case "h":
            ShowStatus("a(dd), s(ave), l(oad), r(emove), (e)dit, (h)elp, (rand)om output, (def)ault output, f(ind)",)

        case "rand":
            ShowStatus("Random mode activated")
            _random_output = True
            _find_results_output = False
        
        case "def":
            ShowStatus("Default mode activated")
            _random_output = False
            _find_results_output = False
        
        case "f":
            ShowStatus("Enter words to find: ")
            _find_results_output = True
            _random_output = False
            _search_word = input("Word to find: ")
             
