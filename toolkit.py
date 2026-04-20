#!/usr/bin/env python3

import os
import subprocess

# ANSI color codes
RED = "\033[91m"
ORANGE = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

def print_result(severity, message):
    if severity == "HIGH":
        print(f"{RED}[HIGH] {message}{RESET}")
    elif severity == "MEDIUM":
        print(f"{ORANGE}[MEDIUM] {message}{RESET}")
    elif severity == "LOW":
        print(f"{GREEN}[LOW] {message}{RESET}")

# ----------------------------
# Check 1: SUID Files
# ----------------------------
def check_suid():
    print("\n[+] Checking SUID files...")
    try:
        result = subprocess.check_output("find / -perm -4000 2>/dev/null", shell=True, text=True)
        for line in result.split("\n"):
            if line.strip():
                print_result("HIGH", f"SUID File Found: {line}")
    except:
        pass

# ----------------------------
# Check 2: Writable /etc/passwd
# ----------------------------
def check_passwd():
    print("\n[+] Checking /etc/passwd permissions...")
    if os.access("/etc/passwd", os.W_OK):
        print_result("HIGH", "/etc/passwd is writable!")
    else:
        print_result("LOW", "/etc/passwd is not writable")

# ----------------------------
# Check 3: Sudo Permissions
# ----------------------------
def check_sudo():
    print("\n[+] Checking sudo permissions...")
    try:
        result = subprocess.check_output("sudo -l", shell=True, text=True)
        print_result("MEDIUM", "User has sudo permissions:")
        print(result)
    except:
        print_result("LOW", "No sudo permissions found")

# ----------------------------
# Check 4: Writable Files in /etc
# ----------------------------
def check_writable_etc():
    print("\n[+] Checking writable files in /etc...")
    try:
        result = subprocess.check_output("find /etc -writable 2>/dev/null", shell=True, text=True)
        for line in result.split("\n"):
            if line.strip():
                print_result("MEDIUM", f"Writable file: {line}")
    except:
        pass

# ----------------------------
# Check 5: Running Services as Root
# ----------------------------
def check_services():
    print("\n[+] Checking services running as root...")
    try:
        result = subprocess.check_output("ps aux | grep root", shell=True, text=True)
        print_result("LOW", "Processes running as root:")
        print(result)
    except:
        pass

# ----------------------------
# MAIN FUNCTION
# ----------------------------
def main():
    print(f"{ORANGE}=== Linux Privilege Escalation Automation Toolkit ==={RESET}")
    
    check_suid()
    check_passwd()
    check_sudo()
    check_writable_etc()
    check_services()

    print(f"\n{GREEN}[✔] Scan Completed{RESET}")

if __name__ == "__main__":
    main()
