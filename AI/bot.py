import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from transformers import pipeline

# Замените 'YOUR_API_TOKEN' на ваш токен API, полученный от BotFather
API_TOKEN = '6443339704:AAHdiXXhN-gl5kv5Byxc3WarDwEhYShFDdQ'

# Установим пайплайны для задач
classifier = pipeline('sentiment-analysis')
generator = pipeline('text-generation', model='gpt2')
translator = pipeline('translation_en_to_fr')

# Настраиваем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Функции для обработки команд
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, который может классифицировать текст, генерировать текст и переводить текст. Используйте команды /classify, /generate или /translate.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Помощь: используйте команды /classify <текст>, /generate <текст> или /translate <текст>.')

def classify_text(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    result = classifier(text)
    update.message.reply_text(result[0]['label'])

def generate_text(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    result = generator(text, max_length=50)
    update.message.reply_text(result[0]['generated_text'])

def translate_text(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    result = translator(text)
    update.message.reply_text(result[0]['translation_text'])

def main() -> None:
    updater = Updater(API_TOKEN)
    
    dispatcher = updater.dispatcher

    # Обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("classify", classify_text))
    dispatcher.add_handler(CommandHandler("generate", generate_text))
    dispatcher.add_handler(CommandHandler("translate", translate_text))

    # Запуск бота
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
