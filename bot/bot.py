from telegram.ext import Application,CommandHandler,CallbackQueryHandler
from cfg.settings import BOT_TOKEN
from .handlers import start_command,button_handler

class TgBot:
    def __init__(self):
        self.application = Application.builder().token(BOT_TOKEN).build()
        self._setup_handlers()

    def _setup_handlers(self):
        self.application.add_handler(CommandHandler("start",start_command))
        self.application.add_handler(CallbackQueryHandler(button_handler))

    def run(self):
        print("START")
        self.application.run_polling()