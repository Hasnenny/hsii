from googlesearch import search
import telebot

bot = telebot.TeleBot("8159522542:AAEUHnph_ah7I4O9JvrHTM9rd_QNP3WW_cI")

@bot.message_handler(commands=['search'])
def ask_book(message):
    msg = bot.send_message(message.chat.id, "📘 اكتب اسم الكتاب الذي تبحث عنه:")
    bot.register_next_step_handler(msg, search_book)

def search_book(message):
    query = f"{message.text} تحميل PDF"
    try:
        results = list(search(query, num_results=5, lang="ar"))

        if results:
            reply = "🔍 روابط البحث:\n\n"
            for link in results:
                reply += f"🔗 {link}\n"
            bot.send_message(message.chat.id, reply)
        else:
            bot.send_message(message.chat.id, "❌ لم أجد نتائج.")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ خطأ أثناء البحث:\n{e}")

bot.infinity_polling()