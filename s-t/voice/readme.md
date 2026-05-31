# Voices Folder

This folder contains Piper text-to-speech voices used by Nexis.

## Downloading Voices

1. Visit the Piper voice repository.
2. Download a voice model (`.onnx`) and its matching `.onnx.json` file.
3. Place both files directly in this folder.

Example:

```text
voices/
├── en_US-ryan-low.onnx
├── en_US-ryan-low.onnx.json
├── en_US-lessac-low.onnx
└── en_US-lessac-low.onnx.json
```

## Recommended Voices

### Ryan (Male)

Files:

```text
en_US-ryan-low.onnx
en_US-ryan-low.onnx.json
```

### Lessac (Male)

Files:

```text
en_US-lessac-low.onnx
en_US-lessac-low.onnx.json
```

## Configuration

Edit `CONFIG.json`:

```json
{
    "TTS": {
        "voice": "ryan"
    }
}
```

Available values depend on the voices installed in this folder.

## Notes

* Both the `.onnx` and `.onnx.json` files are required.
* Voice files are not included in the GitHub repository because of their size.
* Additional Piper voices may be installed if desired.
