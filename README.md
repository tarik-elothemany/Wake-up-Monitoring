# Wake-up Monitoring

## Description
This project monitors wake-up events and lock/unlock attempts on a Windows PC. It sends notifications via Telegram whenever a user tries to wake up the PC or enters a PIN/password. This project can enhance your system's security by informing you of any unauthorized access attempts.

## Features
- Monitors successful and failed login attempts.
- Real-time Telegram notifications for any login attempts detected.
- Detects system wake-up events.

## Prerequisites
Before using this project, make sure to install the following tools and libraries:

1. **Python 3.x**  
   Ensure Python is installed. You can download it here: [Python](https://www.python.org/)

2. **Python Libraries**  
   Install the required libraries by running the following command:
   ```bash
   pip install requests pywin32
