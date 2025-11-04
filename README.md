🤖 PC MANAGE

Telegram bot for monitoring the status of your computer in real time. Get information about the system, network, processes, and even screenshots directly in Telegram!
✨ Capabilities

    System information - OS, processor, memory, disks

    Network information - IP addresses, statistics, interfaces

    📊 Process monitoring - top processes by CPU and memory

    📸 Screen Screenshots - instant desktop snapshots

    📈 System status - visual loading indicators

    , Auto -startup - automatic startup with Windows

🛠 Installation
1. Cloning the repository


git clone <repository url>
cd computer_monitor_bot

2. Creating a virtual
python environment -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

3. Setting up the bot
Getting a bot token:

    Find @BotFather on Telegram

    Send /newbot

    Follow the instructions and get a token.

Creating a settings file:

Create a file .env at the root of the project:
env

BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz0123456789
ADMIN_IDS=123456789,987654321

4. Launching the bot
Manual start-up:

python main.py

Automatic Startup (Windows):

start_bot.bat
start_bot_hidden.vbs for a quiet start

, Auto-upload settings
Method 1: Through the startup folder

    Press Win + R

    Enter shell:startup

    Copy the start_bot.bat to the folder that opens

Method 2: Through the Task Scheduler

    Win + R → taskschd.msc

    Create a simple task

    The trigger: "When logging into Windows"

    Action: "Program launch" → C:\path\to\project\start_bot.bat

Method 3: Hidden launch (without window)

Add the start_bot_hidden file to the startup.vbs instead .bat

🎯 Use
Bot Commands:

    /start - main menu with buttons

    🖥️ System information - detailed information about the system

    Network information - IP addresses and network statistics

    Processes - top processes for CPU usage

    , Status - the visual status of the system

    , Screenshot - an instant screenshot

Example of system output:


, System information

System:
  OS: Windows 10
  Host: DESKTOP-ABC123
  Architecture: 64-bit
  Opening hours: 2:15:30

Processor:
  Usage: 15%
  Cores: 8
Frequency: 3600 MHz

Memory:
  Usage: 45%
  Total: 16.00 GB
  Used: 7.20 GB

, Technical details
Libraries used:

    python-telegram-bot - working with the Telegram API

    psutil - getting system information

    Pillow - creating screenshots

    requests - getting an external IP address

Supported systems:

    ✅ Windows 10/11

    ✅ Linux (with GUI for screenshots)

    ✅ macOS (theoretically)

Problem solving
The bot does not start:

    Check the file availability .env with a token

    Make sure that all dependencies are installed.

    Check access rights for screenshots

Screenshots don't work:

    Screenshots are not available on server systems without a GUI.

    Screen access rights are required

Network errors:

    Check your internet connection

    Make sure that the bot is not blocked by a firewall.

📄 License

MIT License - free use and modification
🤝 Development
Adding new functionality:

    Create a module in the services folder/

    Add a handler to bot/handlers.py

    Update the menu in start_command()


 If you liked the project, don't forget to give it a star!

Designed with ❤️ for convenient system monitoring
