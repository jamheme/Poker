#!/usr/bin/env python3
import os

def test_system_check():
    print("\nTesting original approach:")
    
    # Recreate the original test environment
    try:
        import requests
        
        # Use the same URL pattern from the original code
        base_urls = [
            'https://dickreuter.com:7778/',
            'https://dickreuter.com:7777/', 
            'http://dickreuter.com:7778/',
            'http://dickreuter.com:7777/'
        ]
        
        for base_url in base_urls:
            print(f"\nTesting {base_url}")
            
            # Test endpoints that were in original code
            endpoints = ['get_internal', 'api', 'status', '']
            
            for endpoint in endpoints:
                try:
                    url = base_url + endpoint
                    response = requests.get(url, timeout=10)
                    print(f"GET {endpoint}: {response.status_code}")
                    if response.text:
                        print(f"Response: {response.text[:200]}")
                except Exception as e:
                    try:
                        response = requests.post(url, timeout=10)
                        print(f"POST {endpoint}: {response.status_code}")
                        if response.text:
                            print(f"Response: {response.text[:200]}")
                    except Exception as e2:
                        if "timeout" not in str(e).lower():
                            print(f"{endpoint}: {str(e)[:50]}")
    
    except Exception as e:
        print(f"Requests not available: {e}")

if __name__ == "__main__":
    test_system_check()
