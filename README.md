# Nexis

Nexis is a lightweight offline voice assistant written in Python.

The goal of the project is to provide a fast and simple assistant that can run entirely on local hardware without requiring cloud services, subscriptions, or internet access for voice processing.

Nexis uses:

* Piper for text-to-speech
* Vosk for speech-to-text
* JSON-based response training
* A configurable wake-word system

## Features

* Offline speech recognition
* Offline text-to-speech
* Wake-word activation
* Configurable voices
* Customizable responses
* Cross-platform Python code
* Lightweight and easy to modify

## How It Works

Nexis continuously listens for a wake word.

When a wake word is detected, the assistant begins listening for a command. The command is processed and matched against its training data before a response is generated and spoken aloud.

All processing happens locally on your device.

## Requirements

* Python 3.11 or newer
* Piper
* Vosk
* A supported Piper voice
* A supported Vosk model

## Installation

### 1. Clone or Download the Project

Download the source code and place it in a folder of your choice.

### 2. Install Python Dependencies

```bash
pip install piper-tts vosk sounddevice
```

Additional dependencies may be required depending on your operating system and audio configuration.

### 3. Download Voice Models

Instructions can be found in:

```text
s-t/voice/README.md
```

### 4. Download Speech Recognition Models

Instructions can be found in:

```text
s-t/vosk/README.md
```

### 5. Configure Nexis

Edit:

```text
CONFIG.json
```

to select your preferred voice, wake word, and model configuration.

## Running Nexis

Start the assistant with:

```bash
python Main.py
```

Once running, say the configured wake word followed by your command.

Example:

```text
Hey Nexis
What is your name?
```

## Project Structure

```text
Main.py        Main application
CONFIG.json    Configuration settings
i-o.json       Response training data
LICENSE.txt    License information
s-t/           Speech-to-text and text-to-speech resources
```

## Design Goals

Nexis was created with a few simple goals:

* Work offline
* Be easy to understand
* Be easy to modify
* Have minimal dependencies
* Run on low-end hardware

The project is intentionally simple and is designed to be a foundation that can be expanded with additional features and integrations.

## License

This project is licensed under the Axion Dev License. See `LICENSE.txt` for details.
