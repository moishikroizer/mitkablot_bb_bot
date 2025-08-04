import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# מזהים מהסביבה
BOTLOG_CHANNEL = '@botlog_1221'
ADMIN_USERNAME = '@moishi_5104'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message.text or "<הודעה ללא טקסט>"

    # פרסום בערוץ
    try:
        channel_text = "📥 הודעה חדשה שהתקבלה:

{}".format(message)
        await context.bot.send_message(
            chat_id=BOTLOG_CHANNEL,
            text=channel_text
        )
    except Exception as e:
        print("שגיאה בשליחת הודעה לערוץ:", e)

    # שליחת שם המשתמש למנהל
    try:
        username = user.username or f"ID:{user.id}"
        admin_text = "התקבלה הודעה מ: @{}".format(username)
        await context.bot.send_message(
            chat_id=ADMIN_USERNAME,
            text=admin_text
        )
    except Exception as e:
        print("שגיאה בשליחת שם משתמש למנהל:", e)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()
