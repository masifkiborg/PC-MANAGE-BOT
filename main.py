import os,sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bot.bot import TgBot

from cfg.settings import BOT_TOKEN

def main():
    if not BOT_TOKEN:
        print("LAUNCH ERROR. BOT_TOKEN is missing")
        print("Create .env file and add BOT_TOKEN=your_bot_token")
        return
    bot=TgBot()
    bot.run()

if __name__ == "__main__":
    main()