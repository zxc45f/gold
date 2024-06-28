import telebot

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram Bot token
bot = telebot.TeleBot('7380171310:AAFAhKYwYxjvTY7H6EDkTjJj6OXNyvPvKq4')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا! أنا بوتك الشخصي. أرسل /photo للحصول على صورة من Pinterest.")

@bot.message_handler(commands=['photo'])
def send_photo(message):
    bot.reply_to(message, "عذرًا، لا يمكنني جلب الصور من Pinterest حاليًا بسبب عدم توفر API key.")

bot.polling()
