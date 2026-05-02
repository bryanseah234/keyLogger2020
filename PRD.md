# PRD: keyLogger2020

## Overview
A Python keylogger for educational and security research purposes. Demonstrates how malware can capture keystrokes, persist across reboots via Windows Startup folder injection, and self-propagate into other Python files. This code is shared to educate developers and security professionals about malware patterns — not for deployment against any system without explicit written consent.

## Goals
- Log all keystrokes to a hidden log file on Windows
- Auto-install to Windows Startup folder for persistence
- Demonstrate self-propagation into other `.py`/`.pyw` files in the user's home directory
- Run silently in the background (no visible window)

## Non-Goals
- Exfiltration of logs over network (logs are local only)
- Cross-platform support (Windows only)
- Anti-detection / obfuscation techniques
- Anything beyond educational demonstration

## User Stories
- As a security researcher, I want to understand how keyloggers achieve persistence to build better defenses.
- As a developer, I want to see what startup-folder injection looks like in code so I can detect it in audits.
- As a CTF participant, I want to understand malware patterns for reverse engineering challenges.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: `pynput` (pip), `logging` (stdlib), `threading` (stdlib), `shutil`, `glob`, `os`, `sys`
- **Platform**: Windows only

## Architecture
```
keyLogger2020/
└── keylogger.pyw    # main script (hidden window extension)
```

**Execution flow:**
1. Copy self to `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\` for persistence
2. Walk `C:\Users\{username}\` and prepend own code to any uninfected `.py`/`.pyw` files
3. Create log directory at `%APPDATA%\zzz\`
4. Start `logging` module writing keystrokes to `logs.txt`
5. Start `pynput.keyboard.Listener` capturing all `on_press` events
6. Run both threads as daemons

## Features (detailed)

### Keystroke Logging
- Uses `pynput.keyboard.Listener(on_press=...)` to capture all key events
- Logs to `%APPDATA%\zzz\logs.txt` with timestamp via Python `logging` module
- Runs in a daemon thread

### Startup Persistence
- Copies `keylogger.py` to Windows Startup folder using `shutil.copyfile`
- Executes automatically on every user login

### Self-Propagation
- Walks `C:\Users\{username}\` recursively
- For each `.py` and `.pyw` file that doesn't already contain `#start` marker:
  - Prepends own source code (lines between `#start` and `#end` markers)
  - Infected files will run the keylogger when executed

### Hidden Execution
- Uses `.pyw` extension — Python runs without a console window on Windows

## Data / Config
| Item | Description |
|------|-------------|
| Log file | `C:\Users\{user}\AppData\Roaming\zzz\logs.txt` |
| Startup path | `C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\` |
| Propagation root | `C:\Users\{user}\` |

No config file — all paths are computed from `os.getlogin()`.

## Deployment / Run
```bash
# Educational / authorized use only
pip install pynput
python keylogger.pyw
```

## Constraints & Notes
- **LEGAL WARNING**: Deploying this on any system without explicit written authorization from the owner is illegal under computer fraud laws in virtually every jurisdiction (CFAA in US, Computer Misuse Act in UK/SG, etc.)
- **Educational only**: the code is published to demonstrate malware patterns, not to enable harm
- **Windows only**: Startup folder path and `os.getlogin()` behavior are Windows-specific
- **Detection**: modern Windows Defender detects this as malware — expected behavior
- **Log growth**: no log rotation; `logs.txt` will grow indefinitely
