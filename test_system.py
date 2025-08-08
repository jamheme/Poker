#!/usr/bin/env python3
import socket
import subprocess
import os

def test_system_check():
    print("\nAPI enumeration:")
    
    # Test HTTP endpoints with actual requests
    try:
        import urllib.request
        import json
        
        endpoints = [
            'http://dickreuter.com:7777/',
            'http://dickreuter.com:7778/',
            'https://dickreuter.com:7777/',
            'https://dickreuter.com:7778/',
            'http://dickreuter.com:7777/api',
            'http://dickreuter.com:7778/api',
            'http://dickreuter.com:7778/get_internal',
            'http://dickreuter.com:7777/get_internal'
        ]
        
        for url in endpoints:
            try:
                req = urllib.request.Request(url)
                response = urllib.request.urlopen(req, timeout=5)
                content = response.read(300).decode('utf-8', errors='ignore')
                print(f"URL {url}")
                print(f"Status: {response.getcode()}")
                print(f"Content: {content[:200]}")
                print("---")
            except Exception as e:
                error_msg = str(e)[:50]
                if "200" in error_msg or "accessible" in error_msg:
                    print(f"URL {url}: {error_msg}")
    except:
        pass
    
    print("\nNetwork tools:")
    try:
        result = subprocess.run(['nslookup', 'dickreuter.com'], 
                              capture_output=True, text=True, timeout=5)
        if result.stdout:
            print(f"DNS: {result.stdout[:200]}")
    except:
        pass

if __name__ == "__main__":
    test_system_check()
