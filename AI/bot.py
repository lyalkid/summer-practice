import telebot
from transformers import pipeline

# Замените 'YOUR_API_TOKEN' на ваш токен API, полученный от BotFather

API_TOKEN = '6443339704:AAHdiXXhN-gl5kv5Byxc3WarDwEhYShFDdQ'
bot = telebot.TeleBot(API_TOKEN)

# Создаем пайплайны для задач
classifier = pipeline('sentiment-analysis')
generator = pipeline('text-generation', model='gpt2')
translator = pipeline('translation_en_to_fr')

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который может классифицировать текст, генерировать текст и переводить текст. Используйте команды /classify, /generate или /translate.")

# Команда /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Помощь: используйте команды /classify <текст>, /generate <текст> или /translate <текст>.")

# Команда /classify
@bot.message_handler(commands=['classify'])
def classify_text(message):
    text = message.text[len('/classify '):].strip()
    if text:
        result = classifier(text)
        bot.reply_to(message, result[0]['label'])
    else:
        bot.reply_to(message, "Пожалуйста, предоставьте текст для классификации.")

# Команда /generate
@bot.message_handler(commands=['generate'])
def generate_text(message):
    text = message.text[len('/generate '):].strip()
    if text:
        result = generator(text, max_length=50)
        bot.reply_to(message, result[0]['generated_text'])
    else:
        bot.reply_to(message, "Пожалуйста, предоставьте текст для генерации.")

# Команда /translate
@bot.message_handler(commands=['translate'])
def translate_text(message):
    text = message.text[len('/translate '):].strip()
    if text:
        result = translator(text)
        bot.reply_to(message, result[0]['translation_text'])
    else:
        bot.reply_to(message, "Пожалуйста, предоставьте текст для перевода.")

# Запуск бота
bot.polling()
