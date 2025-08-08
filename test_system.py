#!/usr/bin/env python3
import socket

def test_system_check():
    print("\nTesting actual access vs connectivity:")
    
    print("TCP connectivity test:")
    services = [
        ('dickreuter.com', 22, 'SSH'),
        ('dickreuter.com', 80, 'HTTP'),
        ('dickreuter.com', 443, 'HTTPS'),
        ('dickreuter.com', 7777, 'API-7777'),
        ('dickreuter.com', 7778, 'API-7778'),
        ('dickreuter.com', 27017, 'MongoDB')
    ]
    
    for host, port, service in services:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((host, port))
            status = "PORT OPEN" if result == 0 else "PORT CLOSED"
            print(f"  {service} ({port}): {status}")
            sock.close()
        except Exception as e:
            print(f"  {service} ({port}): ERROR - {e}")
    
    print("\nWhat this means:")
    print("  - TCP connect = Port is open, firewall allows")
    print("  - Does NOT mean we have access to the machine")
    print("  - Does NOT mean we can execute commands")
    print("  - Does NOT mean we can read data")
    
    print("\nWe are in:")
    print("  - GitHub Actions runner (Azure VM)")
    print("  - Can reach dickreuter.com ports")
    print("  - But cannot actually access the server")

if __name__ == "__main__":
    test_system_check()
