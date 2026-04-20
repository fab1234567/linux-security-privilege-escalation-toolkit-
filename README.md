# 🔐 Linux Privilege Escalation Automation Toolkit

A lightweight Python-based security tool that automates common Linux privilege escalation checks.

## 🚀 Features

- 🔴 Detects SUID binaries
- 🔴 Checks writable /etc/passwd
- 🟠 Identifies sudo privileges
- 🟠 Finds writable configuration files
- 🟢 Lists root processes

## 🎨 Severity Color Coding

| Severity | Color |
|----------|------|
| HIGH     | 🔴 Red |
| MEDIUM   | 🟠 Orange |
| LOW      | 🟢 Green |

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/linux-privesc-toolkit.git
cd linux-privesc-toolkit
chmod +x privesc_tool.py
```

## ▶️ Usage

```bash
python3 privesc_tool.py
```

## 📌 Example Output

```
[HIGH] SUID File: /usr/bin/passwd
[MEDIUM] Writable file: /etc/cron.d/example
[LOW] Secure permissions on /etc/passwd
```

## ⚠️ Disclaimer

This tool is for educational and authorized security testing purposes only.  
Do not use it on systems without permission.

## 👨‍💻 Author

Jerin James
