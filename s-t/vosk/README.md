# Vosk Folder

This folder contains speech-to-text models used by Nexis.

## Downloading a Model

Download the Vosk English model and extract it into this folder.

Recommended model:

```text
vosk-model-small-en-us-0.15
```

After extraction the structure should look like:

```text
vosk/
└── vosk-model-small-en-us-0.15/
    ├── am/
    ├── conf/
    ├── graph/
    ├── ivector/
    └── ...
```

## Configuration

Edit `CONFIG.json`:

```json
{
    "STT": {
        "model": "vosk-model-small-en-us-0.15"
    }
}
```

## Notes

* The model folder must remain intact.
* Do not move files out of the model directory.
* Models are not included in the GitHub repository because of their size.
* Larger models may provide better accuracy but require more storage and memory.
