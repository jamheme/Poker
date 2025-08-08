#!/usr/bin/env python3
import socket
import subprocess
import os

def test_system_check():
    print("\nDatabase check:")
    ports = [27017, 5432, 3306, 6379]
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('127.0.0.1', port))
            if result == 0:
                print(f"Port {port} open")
            sock.close()
        except:
            pass
    
    print("\nProduction access:")
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
    
    print("\nNetwork scan:")
    targets = ['10.1.0.1', '10.1.0.10']
    for ip in targets:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, 22))
            if result == 0:
                print(f"Host {ip} SSH open")
            sock.close()
        except:
            pass
    
    print("\nTools:")
    tools = ['psql', 'mongo', 'mysql']
    for tool in tools:
        try:
            result = subprocess.run(['where', tool], capture_output=True, text=True, timeout=2)
            if result.returncode == 0:
                print(f"{tool} available")
        except:
            pass

if __name__ == "__main__":
    test_system_check()
