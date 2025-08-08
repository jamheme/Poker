#!/usr/bin/env python3
import subprocess
import json

def test_system_check():
    print("\nTesting with discovered authentication:")
    
    try:
        subprocess.run(['pip', 'install', 'requests'], capture_output=True, timeout=20)
        import requests
        
        base_url = "https://dickreuter.com:7778/"
        
        print("1. Attempting login to get valid token:")
        
        # Try to get token first
        login_data = {
            "email": "junio_134679@outlook.com",
            "password": "winning22"
        }
        
        try:
            print(f"   Sending POST to {base_url}get_login")
            response = requests.post(
                base_url + "get_login", 
                json=login_data,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            
            print(f"   Login response: {response.status_code}")
            
            if response.status_code == 200:
                print("   SUCCESS! Got login response")
                token_data = response.json()
                print(f"   Token data: {token_data}")
                
                # Extract token if available
                token = None
                if isinstance(token_data, dict):
                    token = token_data.get('token') or token_data.get('access_token') or token_data.get('jwt')
                
                if token:
                    print(f"   Found token: {token[:50]}...")
                    
                    # Now try get_internal with authentication
                    print("\n2. Trying get_internal with token:")
                    
                    auth_headers = {
                        'Authorization': f'Bearer {token}',
                        'Content-Type': 'application/json'
                    }
                    
                    internal_response = requests.post(
                        base_url + "get_internal",
                        headers=auth_headers,
                        timeout=10
                    )
                    
                    print(f"   get_internal with auth: {internal_response.status_code}")
                    
                    if internal_response.status_code == 200:
                        print("   SUCCESS! Got internal data")
                        internal_data = internal_response.json()
                        print(f"   Internal data: {internal_data}")
                    else:
                        print(f"   Auth failed: {internal_response.text[:200]}")
                else:
                    print("   No token found in response")
                    print(f"   Raw response: {response.text[:300]}")
                    
            else:
                print(f"   Login failed: {response.text[:200]}")
                
        except Exception as login_error:
            print(f"   Login request failed: {login_error}")
            
        print("\n3. Alternative auth methods:")
        
        # Try basic auth with email/password
        try:
            from requests.auth import HTTPBasicAuth
            auth = HTTPBasicAuth('junio_134679@outlook.com', 'winning22')
            
            response = requests.post(
                base_url + "get_internal",
                auth=auth,
                timeout=5
            )
            print(f"   Basic auth result: {response.status_code}")
            
        except Exception as e:
            print(f"   Basic auth failed: {e}")
            
        # Try with computer name header
        try:
            headers = {
                'X-Computer-Name': 'NICOLAS-SURFACE',
                'Computer-Name': 'NICOLAS-SURFACE',
                'Host-Name': 'NICOLAS-SURFACE'
            }
            
            response = requests.post(
                base_url + "get_internal",
                headers=headers,
                timeout=5
            )
            print(f"   Computer name header result: {response.status_code}")
            
        except Exception as e:
            print(f"   Computer name header failed: {e}")
            
    except Exception as e:
        print(f"Setup error: {e}")

if __name__ == "__main__":
    test_system_check()
