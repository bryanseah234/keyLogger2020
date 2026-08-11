# keyLogger2020

Live demo: https://hongyime.github.io/keyLogger2020/

![Project screenshot](./screenshot.png)


# ⚠️ CRITICAL WARNING - CONTAINS MALWARE CHARACTERISTICS ⚠️

**THIS CODE IS FOR EDUCATIONAL PURPOSES ONLY**

This repository contains self-replicating malware code that demonstrates dangerous techniques:
- **Self-replication** (infects all .py files)
- **Persistence mechanisms** (Windows Startup)
- **Keylogging** (captures all keyboard input)
- **Stealth operation** (.pyw extension)

## 🚨 LEGAL WARNING

**DEPLOYING THIS CODE IS ILLEGAL AND UNETHICAL**

Using this code without explicit written authorization is:
- **ILLEGAL** under Computer Fraud and Abuse Act (CFAA) and similar laws worldwide
- **CRIMINAL** - Can result in federal prosecution and imprisonment
- **UNETHICAL** - Violates privacy and trust

**Authorized Use Only:**
- Security research in isolated lab environments
- Educational study of malware techniques
- Penetration testing with written authorization

---

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
git clone https://github.com/hongyime/keyLogger2020.git

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

**THIS SOFTWARE CONTAINS SELF-REPLICATING MALWARE CODE**

This software contains self-propagating code that **WILL** modify other Python files on your system. Running this code will:
- Copy itself to Windows startup folder (persistence)
- Scan and modify ALL `.py` and `.pyw` files in your user directory (self-replication)
- Log all keyboard inputs to hidden directory (data exfiltration)
- Run silently in background (stealth)

**ONLY run this in an isolated/sandboxed environment for educational study.**

**DO NOT:**
- Run on production systems
- Run on systems with important files
- Run without explicit authorization
- Deploy against any system you don't own

## Disclaimer

**FOR EDUCATIONAL PURPOSES ONLY - PROOF OF CONCEPT**

1. ⚠️ **CONTAINS MALWARE CHARACTERISTICS** - Self-replicating keylogger
2. ⚠️ **ILLEGAL WITHOUT AUTHORIZATION** - Using this code without written permission is a federal crime
3. ⚠️ **DANGEROUS** - Will modify files on your system
4. ⚠️ **UNETHICAL** - Violates privacy and trust
5. ⚠️ **USE AT YOUR OWN RISK** - Author is not responsible for any misuse

**Legal Consequences:**
- Computer Fraud and Abuse Act (CFAA) violations
- Wiretap Act violations
- State computer crime laws
- Civil liability for damages
- Criminal prosecution and imprisonment

**This code demonstrates malware techniques for educational purposes only.**

**Always obtain explicit written consent before using on any system.**

## License

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
