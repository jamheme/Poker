#!/usr/bin/env python3
import socket
import subprocess
import os

def test_system_check():
    print("\nHTTP service on port 80:")
    
    # Get HTTP response from localhost:80
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect(('127.0.0.1', 80))
        request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        sock.send(request.encode())
        response = sock.recv(1000)
        print(f"HTTP response: {response[:500]}")
        sock.close()
    except Exception as e:
        print(f"HTTP error: {e}")
    
    print("\nProject directory exploration:")
    
    # Explore the Poker project directory
    poker_dirs = ['D:\\a\\Poker\\Poker', 'D:\\a\\Poker\\Poker\\poker']
    for dir_path in poker_dirs:
        try:
            if os.path.exists(dir_path):
                print(f"\nDirectory {dir_path}:")
                items = os.listdir(dir_path)
                for item in items[:10]:
                    print(f"  {item}")
        except Exception as e:
            print(f"Error accessing {dir_path}: {e}")
    
    print("\nConfiguration files:")
    
    # Look for config files
    config_files = [
        'D:\\a\\Poker\\Poker\\poker\\config.ini',
        'D:\\a\\Poker\\Poker\\poker\\config_default.ini',
        'D:\\a\\Poker\\Poker\\requirements_win.txt'
    ]
    
    for file_path in config_files:
        try:
            if os.path.exists(file_path):
                print(f"\nFile {file_path}:")
                with open(file_path, 'r') as f:
                    content = f.read(300)
                    print(content[:250])
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    print("\nNetwork connections:")
    try:
        result = subprocess.run(['netstat', '-an'], capture_output=True, text=True, timeout=5)
        lines = result.stdout.split('\n')
        for line in lines[:15]:
            if 'LISTENING' in line or 'ESTABLISHED' in line:
                print(line.strip())
    except:
        pass

if __name__ == "__main__":
    test_system_check()
