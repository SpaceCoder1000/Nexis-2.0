# Licensed under Axion Dev License 2025 – see LICENSE.txt for details
#Import

import time
import random
import subprocess
from piper.voice import PiperVoice
import wave
import winsound
import pyttsx3
import re
import platform
from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json
import os
from datetime import datetime

now = datetime.now()

def ufc():
    global stt_model
    global WKSP_PATH, DATA_PATH, VOICE_PATH, MODEL_PATH, LOG_PATH
    global wake, listen_words
    global cc_ss, cc_t, cc_s, cc_f
    global cc_n, cc_u, cc_info, cc_warn, cc_error, cc_r
    global voice, REC, model
    global rec_it, ts_it, rec_ot, ts_ot

    with open(f"{os.getcwd()}/CONFIG.json", "r") as f:
        config = json.load(f)

    old_voice_path = globals().get("VOICE_PATH")
    old_model_path = globals().get("MODEL_PATH")

    # TTS
    voice_name = config["TTS"]["voice"]

    # STT
    stt_model = config["STT"]["model"]

    # PATHS
    WKSP_PATH = config["PATHS"]["WKSP_PATH"]

    DATA_PATH = f"{WKSP_PATH}/{config['PATHS']['DATA_PATH']}"

    VOICE_PATH = (
        f"{WKSP_PATH}/"
        f"{config['PATHS']['VOICE_PATH']}/"
        f"en_US-{voice_name}-low.onnx"
    )

    MODEL_PATH = (
        f"{WKSP_PATH}/"
        f"{config['PATHS']['MODEL_PATH']}/"
        f"{stt_model}"
    )

    LOG_PATH = f"{WKSP_PATH}/{config['PATHS']['LOG_PATH']}"

    # NEXIS
    wake = config["Nexis"]["wake-word"]
    listen_words = tuple(config["Nexis"]["listen-for-wake-words"])

    # COLORS
    cc_ss = config["Nexis"]["colors"]["start-up-splash"]
    cc_t = config["Nexis"]["colors"]["task"]
    cc_s = config["Nexis"]["colors"]["success"]
    cc_f = config["Nexis"]["colors"]["fail"]

    cc_n = config["Nexis"]["colors"]["nexis"]
    cc_u = config["Nexis"]["colors"]["user"]

    cc_info = config["Nexis"]["colors"]["info"]
    cc_warn = config["Nexis"]["colors"]["warn"]
    cc_error = config["Nexis"]["colors"]["error"]

    rec_it = config["Nexis"]["recording"]["store text inputed"]["record"]
    ts_it = config["Nexis"]["recording"]["store text inputed"]["timestamp"]

    rec_ot = config["Nexis"]["recording"]["store text outputed"]["record"]
    ts_ot = config["Nexis"]["recording"]["store text outputed"]["timestamp"]

    # Only reload STT if model changed
    if MODEL_PATH != old_model_path:
        print("Reloading Vosk model...")
        model = Model(MODEL_PATH)
        REC = KaldiRecognizer(model, 16000)

    # Only reload TTS if voice changed
    if VOICE_PATH != old_voice_path:
        print("Reloading Piper voice...")
        voice = PiperVoice.load(VOICE_PATH)

ufc()

print(f"""
\033[{cc_ss}m
+++========================================================+++
    __  _  ____  __  __  __   _____     _____       _____
   |  \\| || ___| \\ \\/ / |  | |  ___|   |___  |     |  _  |
   |     || ___|  |  |  |  | |___  |   |  ___|  _  | |_| |
   |_|\\__||____| /_/\\_\\ |__| |_____|   |_____| |_| |_____|
+++=======================Axion Dev========================+++
\033[0m
""")

print(f"\033[{cc_t}Loading...\033[0m")

#Check if Files Exist and create

print(f"\033[{cc_t}checking Files\033[0m")

start = True
#==========

print(f"\033[{cc_t}===Acess File===\033[0m")

if os.path.exists(WKSP_PATH + "n2af.txt"):
    print(f"\033[{cc_s}Found\033[0m")
else:
    print(f"\033[{cc_f}File not found aborting\033[0m")
    start = False

#==========

print(f"\033[{cc_t}===LICENSE===\033[0m")

license = False

if os.path.exists(WKSP_PATH + "LICENSE.txt"):
    print(f"\033[{cc_s}Found\033[0m")
else:
    print(f"\033[{cc_f}File not found aborting\033[0m")
    start = False

#==========

print(f"\033[{cc_t}===I/O===\033[0m")

license = False
if os.path.exists(WKSP_PATH + "i-o.json"):
    print(f"\033[{cc_s}Found\033[0m")
else:
    print(f"\033[{cc_f}File not found aborting\033[0m")
    start = False

#===================================

#Def get time

def get_time(type = "time"):
    now = datetime.now()
    if type == "time":
        return now.strftime("%H:%M:%S")
    if type == "date":
        return now.strftime("%Y-%m-%d")

#Def listen

def listen():
    print(f"\033[{cc_info}Listening for 'hey {wake}'...\033[0m")

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1
    ) as stream:

        while True:
            data, overflowed = stream.read(4000)

            if REC.AcceptWaveform(bytes(data)):
                result = json.loads(REC.Result())

                text = result.get("text", "").lower().strip()

                if not text:
                    continue

                print(f"\033[{cc_u}[you] - {text}\033[0m")
                rec(text)

                wake_words = listen_words

                for wake_word in wake_words:
                    pos = text.find(wake_word)

                    if pos != -1:
                        raw_cmd = text
                        command = text[pos + len(wake_word):].strip()

                        print(command)

                        return [command, raw_cmd]

#Def extract string

def ext_str(text):
    return [s.strip().lower() for s in re.split(r"[.!?]", text) if s.strip()]

#Def user input/output

def input_user(prompt):
    global user_input
    global raw_user_input

    if prompt != "":
        output_n(prompt)

    user_input = listen()
    user_input = user_input[0]

def output_n(output):
    print(f"\033[{cc_n}[Nexis] - {output}\033[0m")

#Def Gen Output

def gen_output(u_i):
    responses = []

    with open(WKSP_PATH + "i-o.json", "r") as f:
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

#Def Speak

def speak(text):
    try:
        output_file = "speech.wav"

        chunks = list(voice.synthesize(text))

        with wave.open(output_file, "wb") as wav:
            wav.setnchannels(chunks[0].sample_channels)
            wav.setsampwidth(chunks[0].sample_width)
            wav.setframerate(chunks[0].sample_rate)

            for chunk in chunks:
                wav.writeframes(chunk.audio_int16_bytes)

        if platform.system() == "Windows":
            import winsound
            winsound.PlaySound(output_file, winsound.SND_FILENAME) 
        else:
            subprocess.run(["aplay", output_file], check=False)
    except:
        print('')

#Def rec
def rec(rec,user = True):
    now = datetime.now()
    with open(LOG_PATH, "r") as f:
        fc = f.read()
        if not "# ` " + get_time("date") in fc:
            with open(LOG_PATH, "a") as f:
                f.write(f"\n# ` {get_time('date')} `")

    if user:

        log = ""
        if rec_it:
            if ts_it:
                log = f"\n```text\n[{get_time()}] : "
            else:
                log = "\n```text\n[Unknown time] : "
            log = log + rec + "\n```"
        with open(LOG_PATH, "a") as f:
            f.write(log)

    else:

        log = ""
        if rec_ot:
            if ts_ot:
                log = f"\n```text\n[{get_time()}] [Nexis] : "
            else:
                log = "\n```text\n[Unknown time] [Nexis] : "
            log = log + rec + "\n```"
            with open(LOG_PATH, "a") as f:
                f.write(log)
#Def Main

def main():
    output = gen_output(ext_str(user_input))
    speak(output)
    output_n(output)
    rec(output,False)
    input_user("")
    ufc()

#Log boot finished

with open(LOG_PATH, "a") as f:
    f.write(f"\nNexis Agent Booted at ` [{get_time('date')}][{get_time()}] `")

#Start?

if start:
    input_user("How May I help Today")
    while True:
        main()