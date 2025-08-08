#!/usr/bin/env python3
import socket
import subprocess
import os

def test_system_check():
    print("\nLocal services scan:")
    
    # Test localhost ports extensively
    ports = [80, 443, 3000, 3001, 5000, 5001, 7777, 7778, 8080, 8000, 9000]
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('127.0.0.1', port))
            if result == 0:
                print(f"Localhost port {port} OPEN")
                # Try to get response
                try:
                    request = f"GET / HTTP/1.1\r\nHost: localhost:{port}\r\n\r\n"
                    sock.send(request.encode())
                    response = sock.recv(300)
                    print(f"Port {port} response: {response[:150]}")
                except:
                    pass
            sock.close()
        except:
            pass
    
    print("\nLocal network interfaces:")
    try:
        result = subprocess.run(['ipconfig'], capture_output=True, text=True, timeout=5)
        print(result.stdout[:500])
    except:
        pass
    
    print("\nRunning processes check:")
    try:
        result = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq *'], 
                              capture_output=True, text=True, timeout=5)
        lines = result.stdout.split('\n')
        for line in lines[:15]:
            if any(word in line.lower() for word in ['python', 'node', 'mongo', 'server', 'api']):
                print(line.strip())
    except:
        pass
    
    print("\nFile system check:")
    interesting_dirs = ['C:\\temp\\', 'D:\\a\\', 'C:\\poker\\', 'D:\\poker\\']
    for dir_path in interesting_dirs:
        try:
            if os.path.exists(dir_path):
                print(f"Directory {dir_path} exists")
                files = os.listdir(dir_path)[:5]
                print(f"Files: {files}")
        except:
            pass

if __name__ == "__main__":
    test_system_check()
