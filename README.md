# 🤖 Computer Monitor Bot

A Telegram bot for real-time computer system monitoring. Get information about your system, network, running processes, and even screenshots directly in Telegram!

## ✨ Features

- 🖥️ **System Information** - OS, CPU, memory, disk usage
- 🌐 **Network Information** - IP addresses, network statistics, interfaces  
- 📊 **Process Monitoring** - top processes by CPU and memory usage
- 📸 **Screenshots** - instant desktop screenshots
- 📈 **System Status** - visual load indicators
- 🔌 **Power Management** - shutdown, restart, hibernate
- 🔔 **Auto-start** - automatic launch with Windows
- 💓 **Keep-alive** - maintains connection to prevent timeouts

## 🛠 Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd computer_monitor_bot
```

### 2. Create Virtual Environment
```bash
# Automatic setup (Windows)
setup_environment.bat

# Or manually:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Bot Configuration

#### Get Bot Token:
1. Find `@BotFather` in Telegram
2. Send `/newbot`
3. Follow instructions and get your token

#### Create Environment File:
Create `.env` file in project root:
```env
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz0123456789
ADMIN_IDS=123456789,987654321
```

### 4. Run the Bot

#### Manual Start:
```bash
python main.py
```

#### Automatic Start (Windows):
```bash
start_bot.bat
```

## 🚀 Auto-start Configuration

### Method 1: Startup Folder
1. Press `Win + R`
2. Type `shell:startup` 
3. Copy `start_bot.bat` to the opened folder

### Method 2: Task Scheduler
1. `Win + R` → `taskschd.msc`
2. Create basic task
3. Trigger: "At log on"
4. Action: "Start program" → `C:\path\to\project\start_bot.bat`

### Method 3: Hidden Start (No Console Window)
Add `start_bot_hidden.vbs` to startup instead of `.bat`


## 🎯 Usage

### Bot Commands:

- `/start` - main menu with buttons
- **🖥️ System Information** - detailed system info
- **🌐 Network Information** - IP addresses and network stats  
- **📊 Processes** - top processes by CPU load
- **📈 Status** - visual system status
- **📸 Screenshot** - instant desktop screenshot
- **🔌 Power Management** - shutdown, restart, hibernate

### Example System Output:
```
🖥️ System Information

System:
  OS: Windows 10
  Host: DESKTOP-ABC123
  Architecture: 64-bit
  Uptime: 2:15:30

Processor:
  Usage: 15%
  Cores: 8
  Frequency: 3600 MHz

Memory:
  Usage: 45%
  Total: 16.00 GB
  Used: 7.20 GB
```

## 🔧 Technical Details

### Used Libraries:
- `python-telegram-bot` - Telegram API integration
- `psutil` - system information gathering
- `Pillow` - screenshot functionality
- `requests` - external IP detection

### Supported Systems:
- ✅ Windows 10/11
- ✅ Linux (with GUI for screenshots)
- ✅ macOS (theoretically)

### Keep-Alive System:
The bot automatically maintains connection to Telegram servers:
- Sends keep-alive requests every 50 seconds
- Prevents timeout disconnections
- Runs in background automatically

## ⚡ Power Management Features

- 🔴 **Shutdown** - after 30 seconds or 1 minute
- 🔄 **Restart** - system reboot
- 💤 **Hibernate** - enter hibernation mode
- ⏹️ **Cancel** - abort scheduled shutdown
- 📋 **System Info** - power management capabilities

## 🐛 Troubleshooting

### Bot Won't Start:
1. Check `.env` file with bot token exists
2. Verify all dependencies are installed
3. Check system permissions

### Screenshots Not Working:
- Not available on server systems without GUI
- Requires screen access permissions

### Network Errors:
- Check internet connection
- Verify bot isn't blocked by firewall


## 📄 License

MIT License - free use and modification

## 🤝 Development




---

**⭐ If you like this project, don't forget to give it a star!**

*Developed with ❤️ for convenient system monitoring*
