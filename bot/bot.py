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

    def _setup_jobs(self):
        job_queue = self.application.job_queue
        job_queue.run_repeating(self._keep_alive, interval=50,first=10)

    async def _keep_alive(self,context):
        try:
            bot_info = await self.application.bot.get_me()
        except Exception as e:
            print()

    def run(self):
        print("START")
        self.application.run_polling()