# Nexis

A simple rule-based console chatbot written in Python by Axion Dev.

## Overview

Nexis is a lightweight terminal assistant that responds to user input by matching keywords against predefined categories stored in a JSON file. Responses are selected randomly from a list associated with the detected category.

## Features

- Keyword-based intent detection
- Randomized responses
- JSON-configurable inputs and outputs
- Simple command-line interface
- Minimal dependencies (Python standard library only)

## Project Structure

```
.
├── Main.py        # Main chatbot application
├── i-o.json       # Input keywords and response database
├── LICENSE.txt    # License information
├── n2af.txt       # Workspace access marker file
└── README.md      # Project information
```

## Requirements

- Python 3.x
- The following files must exist in the configured workspace directory:
  - `i-o.json`
  - `LICENSE.txt`
  - `n2af.txt`

## Configuration

The application currently uses:

```python
WKSP_DIR = "D:/"
```

Ensure all required files are located in that directory, or update the value to match your environment.

## Running the Program

```bash
python Main.py
```

After startup, Nexis will prompt:

```text
[Nexis] - How May I help Today
```

Type messages and receive responses based on matching keywords.

## Supported Categories

The default configuration includes:

- Greetings
- Farewells
- Thanks
- Yes / No
- Help
- Happy
- Sad
- Angry
- Jokes
- Music
- Games
- Food
- Weather
- Time
- Name

These categories can be expanded by editing `i-o.json`.
These are subject to change it is best to check `i-o.json` for the categories.

## How It Works

1. User enters text.
2. Input is converted to lowercase.
3. Nexis searches for matching keywords in `i-o.json`.
4. The first matching category is selected.
5. A random response from that category is returned.

## Known Limitations

- No natural language understanding.
- No persistent memory.
- Workspace path is hardcoded.

## Updates Soon

- Dynamic workspace path.

## License

This project is distributed under the Axion Dev License (2025). See `LICENSE.txt` for details.

## Author

**Axion Dev** (2025)
