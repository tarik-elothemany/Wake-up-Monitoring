# Wake-up Monitoring

## Description
This project monitors wake-up events on a Windows PC using the technique of detecting significant time jumps (greater than 1 minute), as the system time effectively stops during sleep mode. It sends notifications via Telegram when the PC is determined to have woken up from sleep.

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
## Installation

1. **Clone the Repository**  
   Clone the GitHub repository to your local machine:
   ```bash
   git clone https://github.com/tarik-elothemany/Wake-up-Monitoring.git
   cd Wake-up-Monitoring
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

## Configuration
Set up a Telegram bot using [BotFather] and get your TOKEN and CHAT ID.
Update the TOKEN and CHAT_ID in the script.

## Usage
Run the monitoring script:

  ```bash
python monitor.py
