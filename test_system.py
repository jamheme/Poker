#!/usr/bin/env python3
import socket
import subprocess
import os

def test_system_check():
    print("\nWHERE ARE WE? - Complete environment analysis")
    
    print("\n=== INFRASTRUCTURE ===")
    try:
        result = subprocess.run(['ipconfig'], capture_output=True, text=True, timeout=5)
        lines = result.stdout.split('\n')
        for line in lines:
            if 'IPv4' in line or 'DNS Suffix' in line or 'Gateway' in line:
                print(f"  {line.strip()}")
    except:
        pass
    
    print("\n=== WHO OWNS THIS MACHINE ===")
    try:
        # Check cloud metadata (works on AWS/Azure/GCP)
        import urllib.request
        
        # Try Azure metadata
        try:
            req = urllib.request.Request('http://169.254.169.254/metadata/instance?api-version=2021-02-01')
            req.add_header('Metadata', 'true')
            response = urllib.request.urlopen(req, timeout=3)
            print("  AZURE instance detected")
            print(f"  Metadata: {response.read(200)}")
        except:
            pass
            
        # Try AWS metadata
        try:
            response = urllib.request.urlopen('http://169.254.169.254/latest/meta-data/instance-type', timeout=3)
            print("  AWS EC2 instance detected")
            print(f"  Instance type: {response.read().decode()}")
        except:
            pass
            
    except:
        print("  No cloud metadata service detected")
    
    print("\n=== GITHUB ACTIONS CONTEXT ===")
    github_vars = [
        'GITHUB_ACTIONS', 'GITHUB_RUNNER_OS', 'RUNNER_OS', 
        'RUNNER_NAME', 'RUNNER_WORKSPACE', 'GITHUB_WORKSPACE'
    ]
    
    for var in github_vars:
        value = os.environ.get(var, 'Not set')
        print(f"  {var}: {value}")
    
    print("\n=== SYSTEM DETAILS ===")
    try:
        result = subprocess.run(['systeminfo'], capture_output=True, text=True, timeout=10)
        lines = result.stdout.split('\n')
        for line in lines[:15]:
            if line.strip() and any(keyword in line for keyword in ['OS', 'Host', 'Total', 'Available']):
                print(f"  {line.strip()}")
    except:
        pass
    
    print("\n=== NETWORK POSITION ===")
    print("What this connectivity tells us:")
    
    endpoints = [
        ('dickreuter.com', 7777),
        ('dickreuter.com', 7778),
        ('dickreuter.com', 27017),
        ('8.8.8.8', 53),  # Google DNS
        ('1.1.1.1', 53)   # Cloudflare DNS
    ]
    
    for host, port in endpoints:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((host, port))
            status = 'REACHABLE' if result == 0 else 'BLOCKED'
            print(f"  {host}:{port} = {status}")
            sock.close()
        except:
            print(f"  {host}:{port} = ERROR")

if __name__ == "__main__":
    test_system_check()
