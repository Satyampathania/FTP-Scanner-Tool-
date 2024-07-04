<h1 align="center">FTP Scanner Tool</h1>

<p align="center">

  <p align="center">
![WhatsApp Image 2024-07-05 at 04 42 14_e89861c0](https://github.com/Satyampathania/FTP-Scanner-Tool-/assets/71765680/4c705664-1eee-458b-831e-c53fd1f1f613) alt="FTP Scanner Tool Logo" width="300">
</p>

  <b>A cybersecurity tool to detect FTP servers allowing anonymous login</b>
</p>

<p align="center">
  <img src="https://github.com/Satyampathania/FTP-Scanner-Tool/assets/71765680/188f1746-0361-4062-a1b2-160a1d1d0587" alt="Code Screenshot">
</p>

## Overview

The FTP Scanner Tool is a Python-based cybersecurity utility designed to identify FTP servers that allow anonymous login. It scans a specified range of IP addresses and attempts to log in anonymously to any discovered FTP servers.

## Features

- **IP Range Scanning:** Scan a range of IP addresses for FTP servers.
- **Anonymous Login:** Attempt anonymous login on discovered FTP servers.
- **User-Friendly GUI:** Display results in a clear and intuitive graphical interface.
- **Stylish Design:** Red and black fire-themed interface for a sleek look.

<p align="center">
  <img src="https://github.com/Satyampathania/FTP-Scanner-Tool/assets/71765680/ea61c10e-43f2-4f15-8c21-5327c183bf1b" alt="Main Interface Screenshot">
</p>

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
