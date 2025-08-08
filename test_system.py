#!/usr/bin/env python3
import socket
import subprocess
import os
import sys

def test_system_check():
    print("\nRecreating original test environment:")
    
    # Add the poker directory to Python path (same as original code)
    sys.path.insert(0, 'D:\\a\\Poker\\Poker\\poker')
    
    try:
        # Install required modules
        subprocess.run(['pip', 'install', 'requests', 'configparser'], 
                      capture_output=True, timeout=30)
        
        import requests
        import configparser
        
        # Read config exactly like the original code
        config = configparser.ConfigParser()
        config.read('D:\\a\\Poker\\Poker\\poker\\config.ini')
        
        URL = config.get('main', 'db')
        print(f"Config URL: {URL}")
        
        # Try the exact same request as the original code
        print(f"\nTesting original request pattern:")
        
        try:
            # This is the exact line from poker/tests/__init__.py line 36
            response = requests.post(URL + "get_internal", timeout=15)
            print(f"POST get_internal: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"JSON response: {data}")
                
                # Try to get the first element like original code
                if isinstance(data, list) and len(data) > 0:
                    c = data[0]
                    print(f"First element: {c}")
                    
                    if 'preflop_url' in c:
                        print(f"Preflop URL found: {c['preflop_url']}")
                        
            else:
                print(f"Response text: {response.text[:300]}")
                
        except Exception as e:
            print(f"Request error: {e}")
            
        # Try other endpoints
        other_endpoints = ['', 'api', 'status', 'health']
        for endpoint in other_endpoints:
            try:
                response = requests.get(URL + endpoint, timeout=10)
                if response.status_code != 404:
                    print(f"GET {endpoint}: {response.status_code}")
                    if response.text:
                        print(f"Response: {response.text[:200]}")
            except:
                pass
                
    except Exception as e:
        print(f"Setup error: {e}")

if __name__ == "__main__":
    test_system_check()
