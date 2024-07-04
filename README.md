# FTP-Scanner-Tool-

![WhatsApp Image 2024-07-05 at 04 42 14_49c3d1bd](https://github.com/Satyampathania/FTP-Scanner-Tool-/assets/71765680/383cbad2-2a99-4011-b5a0-034a634df337)


## Overview

The Anonymous FTP Scanner is a cybersecurity tool designed to identify FTP servers that allow anonymous login. This tool scans a specified range of IP addresses and attempts to log in to any discovered FTP servers using anonymous credentials. It features a user-friendly GUI with a red and black fire-themed design.

## Features

- Scans a range of IP addresses for FTP servers
- Attempts anonymous login on discovered FTP servers
- Displays results in a user-friendly GUI
- Red and black fire-themed interface

## Screenshots

### CODE
![WhatsApp Image 2024-07-05 at 04 33 42_ae0a5ade](https://github.com/Satyampathania/FTP-Scanner-Tool-/assets/71765680/188f1746-0361-4062-a1b2-160a1d1d0587)


### MAIN INTERFACE
![WhatsApp Image 2024-07-05 at 04 36 24_398c118e](https://github.com/Satyampathania/FTP-Scanner-Tool-/assets/71765680/ea61c10e-43f2-4f15-8c21-5327c183bf1b)


## Getting Started

### Prerequisites

- Python 3.x
- `ftplib` (comes with Python standard library)
- `ipaddress` (comes with Python standard library)
- `tkinter` (comes with Python standard library)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Satyampathania/anonymous-ftp-scanner.git
    cd anonymous-ftp-scanner
    ```

2. Run the script:
    ```bash
    python ftp_scanner.py
    ```

## Usage

1. Enter the start and end IP addresses in the respective fields.
2. Click the "Scan" button to start scanning.
3. View the results in the output text area.

## Example IP Range for Testing

- **Start IP**: `192.168.1.1`
- **End IP**: `192.168.1.5`

This range includes the following IP addresses:
- 192.168.1.1
- 192.168.1.2
- 192.168.1.3
- 192.168.1.4
- 192.168.1.5

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Created by [Satyam pathania](https://github.com/Satyampathania) - feel free to contact me!

