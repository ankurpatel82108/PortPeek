# PortPeek

A lightweight, beginner-friendly TCP port scanner written in pure Python. PortPeek checks a range of ports on a target host and reports which ones are open, along with their likely service name (e.g., port 22 → ssh, port 80 → http).

It's built as an educational tool to help you understand how basic network scanners like `nmap` work under the hood, using nothing but Python's built-in `socket` library.

## ⚠️ Legal & Ethical Use

**Only scan systems you own or have explicit written permission to test.**

Safe practice targets:
- `127.0.0.1` / `localhost` — your own machine
- A virtual machine you control on your own network
- `scanme.nmap.org` — a host the Nmap project set up specifically for people to practice scanning

Scanning systems without permission is illegal in most jurisdictions, even without malicious intent. You are responsible for how you use this tool.

## Features

- Scans a custom range of TCP ports on any target IP or hostname
- Resolves hostnames to IP addresses automatically
- Identifies common service names for open ports
- Reports total scan time and a summary of open ports
- Zero external dependencies — runs with just the Python standard library

## Requirements

- Python 3.6 or higher
- No third-party packages required (see `requirements.txt`)

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/ankurpatel82108/PortPeek.git
   cd PortPeek
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. Install dependencies (none required, but this confirms your environment is ready):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script:
```bash
python3 port_scanner.py
```

You'll be prompted for:
| Prompt | Example | Default |
|---|---|---|
| Target IP or hostname | `127.0.0.1` | `127.0.0.1` |
| Start port | `1` | `1` |
| End port | `1024` | `1024` |

### Example session

```
==================================================
  Simple Port Scanner (educational use only)
==================================================
Target IP or hostname (e.g. 127.0.0.1): 127.0.0.1
Start port (default 1): 1
End port (default 1024): 1024

Scanning 127.0.0.1 from port 1 to 1024
Started at: 2026-09-06 10:00:00
--------------------------------------------------
Port    22 OPEN   (ssh)
Port    80 OPEN   (http)
--------------------------------------------------
Scan finished in 3.42 seconds
Open ports found: 2
  -> [22, 80]
```

## Roadmap / Ideas for Contribution

- [ ] Multithreading for faster scans
- [ ] Banner grabbing to identify running service versions
- [ ] Export results to CSV/JSON
- [ ] Predefined "common ports" scan mode
- [ ] Command-line arguments (argparse) instead of interactive prompts

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is provided for educational purposes only. The author is not responsible for any misuse or damage caused by this tool. Always ensure you have proper authorization before scanning any network or system.
