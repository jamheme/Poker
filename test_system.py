#!/usr/bin/env python3
import socket
import subprocess
import os

def test_system_check():
    print("\nConnection test:")
    
    # Test MongoDB specifically
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex(('dickreuter.com', 27017))
        if result == 0:
            print("MongoDB 27017 accessible")
        sock.close()
    except:
        pass
    
    print("\nMongoDB enumeration:")
    
    # Try different MongoDB commands
    commands = [
        ['mongosh', 'dickreuter.com:27017', '--eval', 'db.runCommand({ping: 1})'],
        ['mongo', 'dickreuter.com:27017', '--eval', 'db.runCommand({ping: 1})'],
        ['mongosh', 'dickreuter.com:27017', '--eval', 'show dbs'],
        ['mongo', 'dickreuter.com:27017', '--eval', 'show dbs']
    ]
    
    for cmd in commands:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            if result.stdout and len(result.stdout.strip()) > 0:
                print(f"Command {cmd[0]} output:")
                print(result.stdout[:300])
                break
        except:
            continue
    
    print("\nHTTP endpoints:")
    
    # Test HTTP endpoints
    try:
        import urllib.request
        urls = [
            'http://dickreuter.com:7777',
            'https://dickreuter.com:7777',
            'http://dickreuter.com:7778',
            'https://dickreuter.com:7778'
        ]
        
        for url in urls:
            try:
                response = urllib.request.urlopen(url, timeout=5)
                content = response.read(200).decode('utf-8', errors='ignore')
                print(f"URL {url}: {response.getcode()}")
                if content:
                    print(f"Content: {content[:100]}")
            except Exception as e:
                pass
    except:
        pass

if __name__ == "__main__":
    test_system_check()
