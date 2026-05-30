# Licensed under Axion Dev License 2025 – see LICENSE.txt for details
import os
import time
import json
import random

#Environment Variables
WKSP_DIR = "D:/" 
data_dir = os.path.join(WKSP_DIR, "data")

print("""
    +++========================================================+++
        __  _  ____  __  __  __   _____     _____       _____
       |  \| || ___| \ \/ / |  | |  ___|   |___  |     |  _  |
       |     || ___|  |  |  |  | |___  |   |  ___|  _  | |_| |
       |_|\__||____| /_/\_\ |__| |_____|   |_____| |_| |_____|
    +++=======================Axion Dev========================+++
    
      """)

time.sleep(1)

#Check if Files Exist and create

print("Checking Files")

start = True
#==========

print("===Acess File===")

if os.path.exists(WKSP_DIR + "n2af.txt"):
    print("Found")
else:
    print("File not found aborting")
    start = False

#==========

print("===LICENSE===")

license = False

if os.path.exists(WKSP_DIR + "LICENSE.txt"):
    print("Found")
else:
    print("File not found aborting")
    start = False

#==========

print("===I/O===")

license = False
if os.path.exists(WKSP_DIR + "i-o.json"):
    print("Found")
else:
    print("File not found aborting")
    start = False

#Def user input/output

def input_user(prompt):
    if prompt != "":
        global user_input
        print("[Nexis] - " + prompt)
        user_input = input("[you] - ")
    else:
        user_input = input("[you] - ")

def output_n(output):
    print("[Nexis] - " + output)

#Def Gen Output

def gen_output(u_i):
    global resp_type
    with open(WKSP_DIR + "i-o.json", "r") as f:
        data = json.load(f)

    u_i = u_i.lower()
    resp_type = None

    for category, words in data["inputs"].items():
        if any(word in u_i for word in words):
            resp_type = category
            break

    if resp_type in data["outputs"]:
        global response
        response = random.choice(data["outputs"][resp_type])
    
    else:
        response = "An error has occured"

#Def Main

def main():
    gen_output(user_input)
    output_n(response)
    input_user("")

#Start?

if start:
    input_user("How May I help Today")
    while True:
        main()