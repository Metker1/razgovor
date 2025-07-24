import telebot

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
bot = telebot.TeleBot(TOKEN)

# Простая функция анализа настроения
def analyze_tone(text):
    positive_keywords = ['рад', 'доволен', 'отлично', 'спасибо', 'хорошо']
    negative_keywords = ['плохо', 'недоволен', 'зря', 'проблема', 'жалоба']
    text_lower = text.lower()
    positive_score = sum(word in text_lower for word in positive_keywords)
    negative_score = sum(word in text_lower for word in negative_keywords)

    if positive_score > negative_score:
        return 'Положительный'
    elif negative_score > positive_score:
        return 'Негативный'
    else:
        return 'Нейтральный'

# Переводим оценку в рекомендации
def get_recommendations(tone):
    if tone == 'Положительный':
        return "Продолжайте в том же духе, добавьте больше дружелюбных выражений."
    elif tone == 'Негативный':
        return "Старайтесь слушать клиента и проявлять эмпатию."
    else:
        return "Можно добавить больше позитивных моментов и поддержки."

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    tone = analyze_tone(text)
    advice = get_recommendations(tone)
    response = f'Оценка тона: {tone}\nРекомендация: {advice}'
    bot.reply_to(message, response)

# Запуск бота
bot.polling()