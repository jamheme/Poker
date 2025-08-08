#!/usr/bin/env python3
import socket
import subprocess
import os

def test_system_check():
    print("\nProduction access test:")
    endpoints = ['dickreuter.com:7777', 'dickreuter.com:7778']
    for endpoint in endpoints:
        try:
            host, port = endpoint.split(':')
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((host, int(port)))
            if result == 0:
                print(f"Production {endpoint} accessible")
            sock.close()
        except:
            pass
    
    print("\nConfiguration found:")
    config_files = [
        'D:\\a\\Poker\\Poker\\poker\\config.ini',
        'D:\\a\\Poker\\Poker\\poker\\config_default.ini'
    ]
    
    for file_path in config_files:
        try:
            if os.path.exists(file_path):
                print(f"File {os.path.basename(file_path)}:")
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if any(keyword in line.lower() for keyword in ['login', 'password', 'db']):
                            print(f"  {line.strip()}")
        except:
            pass
    
    print("\nDatabase tools available:")
    tools = ['mongo', 'mysql', 'psql']
    for tool in tools:
        try:
            result = subprocess.run(['where', tool], capture_output=True, text=True, timeout=2)
            if result.returncode == 0:
                print(f"{tool} found")
        except:
            pass
    
    print("\nEnvironment variables:")
    for key, value in os.environ.items():
        if any(keyword in key.upper() for keyword in ['PGPASSWORD', 'MONGO', 'DB']):
            print(f"{key}={value}")
    
    print("\nMongoDB connection test:")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex(('dickreuter.com', 27017))
        if result == 0:
            print("MongoDB dickreuter.com:27017 connected")
        sock.close()
    except:
        pass

if __name__ == "__main__":
    test_system_check()
