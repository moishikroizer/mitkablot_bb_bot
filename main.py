import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOTLOG_CHANNEL = '@botlog_1221'
ADMIN_USERNAME = '@moishi_5104'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message.text or "<הודעה ללא טקסט>"

    try:
        text_to_channel = "התקבלה הודעה חדשה:\n\n" + message
        await context.bot.send_message(chat_id=BOTLOG_CHANNEL, text=text_to_channel)
    except Exception as e:
        print("שגיאה בשליחה לערוץ:", e)

    try:
        username = user.username or ("ID:" + str(user.id))
        text_to_admin = "התקבלה הודעה מ: @" + username
        await context.bot.send_message(chat_id=ADMIN_USERNAME, text=text_to_admin)
    except Exception as e:
        print("שגיאה בשליחה למנהל:", e)

if __name__ == '__main__':
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
