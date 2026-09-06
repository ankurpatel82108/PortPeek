#!/usr/bin/env python3
"""
Simple Port Scanner - A beginner cybersecurity practice tool
================================================================

WHAT THIS DOES:
Checks a range of ports on a target host to see which ones are "open"
(i.e., something is listening and accepting connections). This is the
same basic idea behind tools like nmap, just much simpler.

LEGAL / ETHICAL NOTE:
Only run this against systems you own or have explicit permission to
test. Good practice targets:
  - 127.0.0.1 / localhost (your own machine)
  - A VM you control on your own network
  - scanme.nmap.org (a host the nmap project set up specifically
    for people to practice scanning)

Scanning systems without permission can be illegal, even if you don't
intend any harm.

HOW IT WORKS:
For each port, we try to open a TCP connection using Python's built-in
`socket` library. If the connection succeeds, the port is open. If it
times out or is refused, we treat it as closed/filtered.
"""

import socket
import sys
from datetime import datetime


def scan_port(target_ip, port, timeout=1):
    """
    Try to connect to a single port on the target.
    Returns True if the port is open, False otherwise.
    """
    # AF_INET = IPv4, SOCK_STREAM = TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        # connect_ex returns 0 on success, an error code otherwise
        result = sock.connect_ex((target_ip, port))
        return result == 0
    except socket.error:
        return False
    finally:
        sock.close()


def get_service_name(port):
    """
    Try to look up the common service name for a port
    (e.g., 80 -> http, 22 -> ssh). Falls back to 'unknown'.
    """
    try:
        return socket.getservbyport(port)
    except OSError:
        return "unknown"


def scan_range(target_ip, start_port, end_port, timeout=1):
    """
    Scan a range of ports and print results as we go.
    """
    print(f"\nScanning {target_ip} from port {start_port} to {end_port}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    open_ports = []
    start_time = datetime.now()

    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port, timeout):
            service = get_service_name(port)
            print(f"Port {port:>5} OPEN   ({service})")
            open_ports.append(port)

    duration = (datetime.now() - start_time).total_seconds()
    print("-" * 50)
    print(f"Scan finished in {duration:.2f} seconds")
    print(f"Open ports found: {len(open_ports)}")
    if open_ports:
        print(f"  -> {open_ports}")
    else:
        print("  -> None")

    return open_ports


def resolve_target(target):
    """
    Convert a hostname (like 'localhost') into an IP address.
    """
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: could not resolve hostname '{target}'")
        sys.exit(1)


def main():
    print("=" * 50)
    print("  Simple Port Scanner (educational use only)")
    print("=" * 50)

    target = input("Target IP or hostname (e.g. 127.0.0.1): ").strip()
    if not target:
        target = "127.0.0.1"

    try:
        start_port = int(input("Start port (default 1): ") or 1)
        end_port = int(input("End port (default 1024): ") or 1024)
    except ValueError:
        print("Ports must be numbers. Exiting.")
        sys.exit(1)

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Ports must be between 1 and 65535.")
        sys.exit(1)

    target_ip = resolve_target(target)
    scan_range(target_ip, start_port, end_port)


if __name__ == "__main__":
    main()
