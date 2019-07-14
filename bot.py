# -*- coding: utf-8 -*-
import telebot
import logging
import sys
# Usage: bot.py [TOKEN]
bot = telebot.TeleBot(sys.argv[1])

logging.basicConfig(filename='pvChat_bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    admins = [user.user.username for user in bot.get_chat_administrators(message.chat.id)]
    if ("t.me/joinchat" in message.text) and (message.from_user.username not in admins):
        bot.delete_message(message.chat.id, message.message_id)


bot.polling(none_stop=True, interval=0)
