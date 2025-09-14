import os
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.getenv("TOKEN")

def welcome(update, context):
    for member in update.message.new_chat_members:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"👋 Welcome {member.first_name}!\n\n"
                 "📌 Here's our write-up:\n"
                 "➡️ Be respectful\n"
                 "➡️ Share knowledge\n"
                 "➡️ Enjoy your stay!"
        )

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

updater.start_polling()
updater.idle()
