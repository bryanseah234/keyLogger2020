# keyLogger2020

A Python-based keylogger for Windows that captures and logs all keyboard inputs.

## Description

keyLogger2020 is a Windows keylogger written in Python that records all keyboard inputs and stores them in a log file. The application runs silently in the background and automatically starts when Windows boots up. This project demonstrates keyboard event handling, logging techniques, and self-replication mechanisms in Python for educational purposes.

## Features

- Captures all keyboard inputs in real-time
- Stores logs with timestamps in a hidden directory
- Auto-starts on Windows startup
- Runs silently in the background using threading
- Lightweight and efficient

## Technologies Used

- Python 3.x
- pynput (keyboard listener library)
- Threading (for background execution)
- Logging (for timestamped log storage)

## Installation

```bash
# Clone the repository
git clone https://github.com/bryanseah234/keyLogger2020.git

# Navigate to project directory
cd keyLogger2020

# Install dependencies
pip install pynput
```

## Usage

```bash
# Run the keylogger
python keylogger.pyw
```

Logs are stored at: `C:\Users\<YourUsername>\AppData\Roaming\zzz\logs.txt`

## ⚠️ Warning

This software contains self-propagating code that may modify other Python files on your system. Running this code will:
- Copy itself to Windows startup folder
- Scan and potentially modify other `.py` and `.pyw` files in your user directory

**Only run this in an isolated/sandboxed environment for educational study.**

## Disclaimer

1. FOR EDUCATIONAL PURPOSES ONLY
2. USE AT YOUR OWN DISCRETION
3. The author is not responsible for any misuse of this software
4. Always obtain proper consent before using on any system
5. This code demonstrates malware techniques - do NOT use maliciously

## License

MIT License

---

**Author:** <a href="https://github.com/bryanseah234">bryanseah234</a>
