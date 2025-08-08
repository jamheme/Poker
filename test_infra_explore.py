#!/usr/bin/env python3
import requests
import socket
import os

def try_aws_metadata():
    print("\n=== AWS METADATA ===")
    try:
        r = requests.get("http://169.254.169.254/latest/meta-data/", timeout=2)
        print("Metadata:", r.text[:200])
    except Exception as e:
        print("Metadata access failed:", e)

def check_docker_socket():
    print("\n=== DOCKER SOCKET ===")
    print("Docker socket exists:", os.path.exists("/var/run/docker.sock"))

def scan_internal_ips():
    print("\n=== SCAN INTERNAL IPs ===")
    base_ranges = ["10.1.0", "10.0.0", "172.16.0", "192.168.0"]
    for base in base_ranges:
        for i in range(1, 5):
            ip = f"{base}.{i}"
            for port in [22, 80, 443, 2375, 10250, 5000, 8080]:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    result = sock.connect_ex((ip, port))
                    sock.close()
                    if result == 0:
                        print(f"Open: {ip}:{port}")
                except:
                    pass

if __name__ == "__main__":
    try_aws_metadata()
    check_docker_socket()
    scan_internal_ips()
