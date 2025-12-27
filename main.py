import telebot
from openai import OpenAI

# Твои ключи (временно, для теста)
BOT_TOKEN = "8560364718:AAFbG3Not_sWxPUIKlRH_X8onLnDHWCbr7w"

client = OpenAI(api_key=OPENAI_KEY)
bot = telebot.TeleBot(BOT_TOKEN)

SYSTEM = "Ты таджикский учитель языков. Объясняй простыми словами, дружелюбно, на таджикском."

@bot.message_handler(func=lambda message: True)
def reply(message):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": message.text}
            ]
        )
        bot.send_message(message.chat.id, completion.choices[0].message.content)
    except Exception:
        bot.send_message(message.chat.id, "Хато шуд. Боз кӯшиш кунед.")

bot.polling()
