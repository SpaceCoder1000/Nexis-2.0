# Licensed under Axion Dev License 2025 – see LICENSE.txt for details

print("""
    \033[34m
    +++========================================================+++
        __  _  ____  __  __  __   _____     _____       _____
       |  \| || ___| \ \/ / |  | |  ___|   |___  |     |  _  |
       |     || ___|  |  |  |  | |___  |   |  ___|  _  | |_| |
       |_|\__||____| /_/\_\ |__| |_____|   |_____| |_| |_____|
    +++=======================Axion Dev========================+++
    \033[0m
      """)

#Import

import os
import time
import json
import random
import subprocess
from piper.voice import PiperVoice
import wave
import winsound
import pyttsx3
import re

#Environment Variables

WKSP_DIR = "D:/" 
data_dir = os.path.join(WKSP_DIR, "data")

#Check if Files Exist and create

print("\033[36mChecking Files\033[0m")

start = True
#==========

print("\033[36m===Acess File===\033[0m")

if os.path.exists(WKSP_DIR + "n2af.txt"):
    print("\033[32mFound\033[0m")
else:
    print("\033[31mFile not found aborting\033[0m")
    start = False

#==========

print("\033[36m===LICENSE===\033[0m")

license = False

if os.path.exists(WKSP_DIR + "LICENSE.txt"):
    print("\033[32mFound\033[0m")
else:
    print("\033[31mFile not found aborting\033[0m")
    start = False

#==========

print("\033[36m===I/O===\033[0m")

license = False
if os.path.exists(WKSP_DIR + "i-o.json"):
    print("\033[32mFound\033[0m")
else:
    print("\033[31mFile not found aborting\033[0m")
    start = False

#===================================

def ext_str(text):
    return [s.strip().lower() for s in re.split(r"[.!?]", text) if s.strip()]

#Def user input/output

def input_user(prompt):
    if prompt != "":
        global user_input
        print("\033[94m" + "[Nexis] - " + prompt)
        user_input = input("\033[92m" + "[you] - " + "\033[0m")
    else:
        user_input = input("\033[92m" + "[you] - " + "\033[0m")

def output_n(output):
    print("\033[94m" + "[Nexis] - " + output + "\033[0m")

#Def Gen Output

def gen_output(u_i):
    responses = []

    with open(WKSP_DIR + "i-o.json", "r") as f:
        data = json.load(f)

    for sentence in u_i:
        sentence = sentence.lower()

        sentence_responses = []

        for category, triggers in data["inputs"].items():

            # Check longest triggers first
            sorted_triggers = sorted(
                triggers,
                key=len,
                reverse=True
            )

            for trigger in sorted_triggers:
                if re.search(r"\b" + re.escape(trigger.lower()) + r"\b", sentence):
                    sentence_responses.append(
                        random.choice(data["outputs"][category])
                    )
                    break

        if sentence_responses:
            responses.append(", ".join(sentence_responses))
        else:
            responses.append("I don't understand")

    return ". ".join(responses) + "."

#Def Main

def main():
    output_n(gen_output(ext_str(user_input)))
    input_user("")

#Start?

if start:
    input_user("How May I help Today")
    while True:
        main()
