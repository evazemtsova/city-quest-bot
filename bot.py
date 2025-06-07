import os
import logging
from datetime import datetime, timedelta
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from geopy.distance import geodesic

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Constants
LOCATION_RADIUS = 50  # meters
INACTIVITY_DAYS = 30

class CityQuestBot:
    def __init__(self):
        self.token = os.getenv('TELEGRAM_BOT_TOKEN')
        if not self.token:
            raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables")

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send welcome message when the command /start is issued."""
        welcome_message = (
            "👋 Добро пожаловать в City Quest Bot!\n\n"
            "Я помогу тебе открыть новые места в Санкт-Петербурге через увлекательный квест.\n"
            "Просто отправь мне свою геолокацию, и мы начнем приключение!\n\n"
            "Правила просты:\n"
            "1. Я буду отправлять тебе загадки о местах в городе\n"
            "2. Твоя задача - найти это место и отправить мне свою геолокацию\n"
            "3. Если ты в радиусе 50 метров от правильного места, я дам тебе следующую загадку\n"
            "4. Всего 10 заданий, которые откроют тебе новые уголки города\n\n"
            "Готов начать? Отправь мне свою геолокацию! 📍"
        )
        await update.message.reply_text(welcome_message)

    async def handle_location(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle the user's location."""
        # TODO: Implement location handling logic
        await update.message.reply_text("Функция проверки локации будет реализована в следующем шаге!")

    def run(self):
        """Start the bot."""
        application = Application.builder().token(self.token).build()

        # Add handlers
        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(MessageHandler(filters.LOCATION, self.handle_location))

        # Start the bot
        application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    bot = CityQuestBot()
    bot.run() 