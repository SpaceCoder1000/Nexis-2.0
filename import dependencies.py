import subprocess
import sys

packages = [
    "vosk",
    "sounddevice",
    "piper-tts",
    "duckduckgo-search"
]

for package in packages:
    print(f"Installing {package}...")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", package]
    )