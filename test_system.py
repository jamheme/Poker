#!/usr/bin/env python3
import socket
import subprocess
import os

def test_system_check():
    print("\nDirect socket test:")
    
    # Test raw socket communication
    for port in [7777, 7778]:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex(('dickreuter.com', port))
            if result == 0:
                print(f"Port {port} connected")
                # Send HTTP request
                request = f"GET / HTTP/1.1\r\nHost: dickreuter.com:{port}\r\n\r\n"
                sock.send(request.encode())
                response = sock.recv(500)
                print(f"Port {port} response: {response[:200]}")
            sock.close()
        except Exception as e:
            print(f"Port {port} error: {e}")
    
    print("\nCurl test:")
    
    # Try with curl if available
    urls = [
        'http://dickreuter.com:7777',
        'http://dickreuter.com:7778',
        'http://52.50.218.30:7777',
        'http://52.50.218.30:7778'
    ]
    
    for url in urls:
        try:
            result = subprocess.run(['curl', '-s', '--connect-timeout', '5', url], 
                                  capture_output=True, text=True, timeout=10)
            if result.stdout:
                print(f"Curl {url}: {result.stdout[:200]}")
        except:
            pass
    
    print("\nPing test:")
    try:
        result = subprocess.run(['ping', '-n', '2', 'dickreuter.com'], 
                              capture_output=True, text=True, timeout=10)
        if result.stdout:
            print(f"Ping: {result.stdout[:300]}")
    except:
        pass

if __name__ == "__main__":
    test_system_check()
