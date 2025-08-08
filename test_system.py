#!/usr/bin/env python3
import os
import sys

def test_system_check():
    print("\nTrying the ORIGINAL approach that should work:")
    
    try:
        # Install what we need
        import subprocess
        subprocess.run(['pip', 'install', 'requests', 'configparser'], 
                      capture_output=True, timeout=30)
        
        import requests
        import configparser
        
        # Use EXACT same config as original
        config_path = 'D:\\a\\Poker\\Poker\\poker\\config.ini'
        if os.path.exists(config_path):
            config = configparser.ConfigParser()
            config.read(config_path)
            URL = config.get('main', 'db')
            print(f"Using config URL: {URL}")
            
            # Try the EXACT same request the original code makes
            print("\nMaking the exact same request as original code:")
            print("POST /get_internal")
            
            try:
                response = requests.post(URL + "get_internal", timeout=15)
                print(f"Status code: {response.status_code}")
                
                if response.status_code == 200:
                    print("SUCCESS! Got response from get_internal")
                    try:
                        data = response.json()
                        print(f"JSON data: {data}")
                        
                        if isinstance(data, list) and len(data) > 0:
                            first_item = data[0]
                            print(f"First item: {first_item}")
                            
                            if 'preflop_url' in first_item:
                                print(f"FOUND preflop_url: {first_item['preflop_url']}")
                                
                    except Exception as json_error:
                        print(f"JSON parse error: {json_error}")
                        print(f"Raw response: {response.text[:500]}")
                        
                else:
                    print(f"Non-200 response: {response.text[:300]}")
                    
            except Exception as request_error:
                print(f"Request failed: {request_error}")
                
        else:
            print("Config file not found, using hardcoded URL")
            URL = "https://dickreuter.com:7778/"
            response = requests.post(URL + "get_internal", timeout=15)
            print(f"Hardcoded URL result: {response.status_code}")
            
    except Exception as e:
        print(f"Setup error: {e}")
        
    print("\nThis is the EXACT request the original tests make!")
    print("If this works, we have the real data access.")

if __name__ == "__main__":
    test_system_check()
