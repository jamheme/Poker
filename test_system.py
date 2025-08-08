#!/usr/bin/env python3
import socket
import subprocess
import os

def test_system_check():
    print("\nMongoDB access:")
    
    # Confirm MongoDB connection
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex(('dickreuter.com', 27017))
        if result == 0:
            print("MongoDB dickreuter.com:27017 connected")
        sock.close()
    except:
        pass
    
    # Check available MongoDB tools
    tools = ['mongosh', 'mongo']
    for tool in tools:
        try:
            result = subprocess.run(['where', tool], capture_output=True, text=True, timeout=3)
            if result.returncode == 0:
                print(f"Tool {tool} found at {result.stdout.strip()}")
        except:
            pass
    
    # Try direct MongoDB connection without auth
    print("\nDirect connection test:")
    try:
        result = subprocess.run([
            'mongo', '--host', 'dickreuter.com', '--port', '27017',
            '--eval', 'print("Connected successfully")'
        ], capture_output=True, text=True, timeout=10)
        if result.stdout:
            print(f"MongoDB response: {result.stdout.strip()}")
        if result.stderr:
            print(f"MongoDB stderr: {result.stderr.strip()}")
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
    
    # Try API endpoints directly
    print("\nAPI test:")
    endpoints = [7777, 7778]
    for port in endpoints:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex(('dickreuter.com', port))
            if result == 0:
                print(f"API port {port} accessible")
            sock.close()
        except:
            pass

if __name__ == "__main__":
    test_system_check()
