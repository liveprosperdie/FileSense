# FileSense 🗂️

A smart file organizer that automatically sorts files into categorized folders — run it once manually or let it watch a folder in the background.

---

## Features

- Organizes files into categories: Images, Videos, Audio, Documents, Code, Archives, and Others
- Two modes: manual (run once) and watch (runs in background)
- Logs every action with timestamps
- Works on any folder, not just Downloads
- Handles permission errors, missing folders, and edge cases gracefully

---

## Project Structure

```
FileSense/
├── main.py          # Entry point with CLI arguments
├── organizer.py     # Core file sorting logic
├── watcher.py       # Background folder watcher
├── config.py        # File type mappings
├── logger.py        # Activity logging
└── logs/
    └── activity.log # Auto-created on first run
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FileSense.git
   cd FileSense
   ```

2. Install dependencies:
   ```bash
   pip install watchdog
   ```

---

## Usage

### Manual Mode
Organizes the folder once and exits.

```bash
python main.py --mode manual
```

You'll be prompted to enter the folder path:
```
Enter the folder to organise: C:\Users\YourName\Downloads
```

### Watch Mode
Watches the folder continuously and organizes new files as they appear. Runs until you press `Ctrl+C`.

```bash
python main.py --mode watch
```

---

## File Categories

| Folder     | Extensions                                      |
|------------|-------------------------------------------------|
| Images     | .jpg, .png, .gif, .svg, .webp                   |
| Videos     | .mp4, .mkv, .mov, .avi                          |
| Audio      | .mp3, .wav, .flac                               |
| Documents  | .pdf, .docx, .txt, .xlsx, .pptx                 |
| Code       | .py, .js, .html, .css, .java, .c               |
| Archives   | .zip, .rar, .tar, .gz                           |
| Others     | Anything that doesn't match the above           |

---

## Logs

Every file move and error is logged automatically to `logs/activity.log` inside the FileSense project folder.

Example log entries:
```
2024-01-15 14:32:10 - INFO - Successfully moved photo.jpg to images folder
2024-01-15 14:32:11 - ERROR - report.pdf can't be moved
```

---

## Adding Custom File Types

Open `config.py` and add extensions to the relevant category:

```python
FILE_TYPES = {
    "images": [".jpg", ".png", ".gif", ".svg", ".webp", ".heic"],  # added .heic
    ...
}
```

---

## Requirements

- Python 3.6+
- watchdog (`pip install watchdog`)
