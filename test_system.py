#!/usr/bin/env python3
import subprocess
import os
import sys

def test_system_check():
    print("\nNormal application behavior simulation:")
    
    try:
        # Install and import like a normal test would
        subprocess.run(['pip', 'install', 'requests'], capture_output=True, timeout=30)
        import requests
        
        # Simulate normal application startup
        print("Simulating poker application initialization...")
        
        # Use User-Agent like a real application
        headers = {
            'User-Agent': 'DeepMind-PokerBot/1.0',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        
        base_url = "https://dickreuter.com:7778/"
        
        # Try a simple health check first
        try:
            response = requests.get(base_url, headers=headers, timeout=5)
            print(f"Health check: {response.status_code}")
        except Exception as e:
            print(f"Health check failed: {e}")
        
        # Simulate the exact sequence from the original tests
        print("\nSimulating test initialization sequence...")
        
        try:
            # This mirrors the original poker/tests/__init__.py logic
            response = requests.post(
                base_url + "get_internal", 
                headers=headers,
                json={},  # Empty JSON payload
                timeout=10
            )
            
            print(f"get_internal response: {response.status_code}")
            
            if response.text:
                print(f"Response content: {response.text[:500]}")
                
        except Exception as e:
            print(f"get_internal failed: {e}")
            
        # Check if we can at least reach the domain
        print("\nBasic connectivity test:")
        try:
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex(('dickreuter.com', 7778))
            print(f"Socket connect result: {result}")
            sock.close()
        except Exception as e:
            print(f"Socket test: {e}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_system_check()
