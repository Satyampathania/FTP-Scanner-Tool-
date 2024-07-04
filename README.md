<h1 align="center">FTP Scanner Tool</h1>

<p align="center">
  <b>A cybersecurity tool to detect FTP servers allowing anonymous login</b>
</p>

## Overview

The FTP Scanner Tool is a Python-based cybersecurity utility designed to identify FTP servers that allow anonymous login. It scans a specified range of IP addresses and attempts to log in anonymously to any discovered FTP servers.

## Features

- **IP Range Scanning:** Scan a range of IP addresses for FTP servers.
- **Anonymous Login:** Attempt anonymous login on discovered FTP servers.
- **User-Friendly GUI:** Display results in a clear and intuitive graphical interface.
- **Stylish Design:** Red and black fire-themed interface for a sleek look.

## Screenshots

<!-- Add screenshots here -->
- ![WhatsApp Image 2024-07-05 at 04 33 42_63d91875](https://github.com/Satyampathania/FTP-Scanner-Tool-/assets/71765680/8d9d039c-72ef-4db8-a82b-e10d344eab19)

- ![WhatsApp Image 2024-07-05 at 04 36 24_590f73d9](https://github.com/Satyampathania/FTP-Scanner-Tool-/assets/71765680/ca237dea-8971-43fa-b566-2b2a7a0f45f0)

## Getting Started

### Prerequisites

- Python 3.x
- `ftplib` (comes with Python standard library)
- `ipaddress` (comes with Python standard library)
- `tkinter` (comes with Python standard library)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Satyampathania/FTP-Scanner-Tool.git
    cd FTP-Scanner-Tool
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

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Created by [Satyam Pathania](https://github.com/Satyampathania) - feel free to contact me!
