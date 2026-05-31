# Licensed under Axion Dev License 2025 – see LICENSE.txt for details

import json
import os

def ufc():
    global voice, stt_model
    global WKSP_PATH, DATA_PATH, VOICE_PATH, MODEL_PATH
    global wake, listen_words
    global cc_ss, cc_t, cc_s, cc_f
    global cc_n, cc_u, cc_info, cc_warn, cc_error, cc_r

    with open(f"{os.getcwd}CONFIG.json", "r") as f:
        config = json.load(f)

    # TTS
    voice = config["TTS"]["voice"]

    # STT
    stt_model = config["STT"]["model"]

    # PATHS
    WKSP_PATH = config["PATHS"]["WKSP_PATH"]

    DATA_PATH = f"{WKSP_PATH}/{config['PATHS']['DATA_PATH']}"

    VOICE_PATH = (
        f"{WKSP_PATH}/"
        f"{config['PATHS']['VOICE_PATH']}/"
        f"en_US-{voice}-low.onnx"
    )

    MODEL_PATH = (
        f"{WKSP_PATH}/"
        f"{config['PATHS']['MODEL_PATH']}/"
        f"{stt_model}"
    )

    # NEXIS
    wake = config["Nexis"]["wake-word"]
    listen_words = config["Nexis"]["listen-for-wake-words"]

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

print(f"""
    \033[{cc_ss}
    +++========================================================+++
        __  _  ____  __  __  __   _____     _____       _____
       |  \| || ___| \ \/ / |  | |  ___|   |___  |     |  _  |
       |     || ___|  |  |  |  | |___  |   |  ___|  _  | |_| |
       |_|\__||____| /_/\_\ |__| |_____|   |_____| |_| |_____|

    +++=======================Axion Dev========================+++
    \033[0m
      """)

print("\033[36m Loading \n \033[0m")

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

#Environment Variables

WKSP_PATH = os.getcwd() 
DATA_PATH = f"{WKSP_PATH}/data"
VOICE_PATH = f"{WKSP_PATH}/voices/en_US-ryan-low.onnx"
MODEL_PATH = f"{WKSP_PATH}/vosk-model-small-un-us-0.15"
model = Model(MODEL_PATH)
REC = KaldiRecognizer(model, 16000)

voice = PiperVoice.load(VOICE_PATH)


#Check if Files Exist and create

print("\033[36mChecking Files\033[0m")

start = True
#==========

print("\033[36m===Acess File===\033[0m")

if os.path.exists(WKSP_PATH + "n2af.txt"):
    print("\033[32mFound\033[0m")
else:
    print("\033[31mFile not found aborting\033[0m")
    start = False

#==========

print("\033[36m===LICENSE===\033[0m")

license = False

if os.path.exists(WKSP_PATH + "LICENSE.txt"):
    print("\033[32mFound\033[0m")
else:
    print("\033[31mFile not found aborting\033[0m")
    start = False

#==========

print("\033[36m===I/O===\033[0m")

license = False
if os.path.exists(WKSP_PATH + "i-o.json"):
    print("\033[32mFound\033[0m")
else:
    print("\033[31mFile not found aborting\033[0m")
    start = False

#===================================

#Def listen

def listen():
    print("\033[93mListening for 'hey nexis'...\033[0m")

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

                print("\033[92m[you] - " + text + "\033[0m")

                wake_words = ("nexus", "texas", "this", "lexus")

                for wake_word in wake_words:
                    pos = text.find(wake_word)

                    if pos != -1:
                        command = text[pos + len(wake_word):].strip()

                        print(command)

                        return command

#Def extract string

def ext_str(text):
    return [s.strip().lower() for s in re.split(r"[.!?]", text) if s.strip()]

#Def user input/output

def input_user(prompt):
    global user_input

    if prompt != "":
        output_n(prompt)

    user_input = listen()

def output_n(output):
    print("\033[94m" + "[Nexis] - " + output + "\033[0m")

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
#Def Main

def main():
    output = gen_output(ext_str(user_input))
    speak(output)
    output_n(output)
    input_user("")
    #ufc("CONFIG.json")

#Start?

if start:
    input_user("How May I help Today")
    while True:
        main()