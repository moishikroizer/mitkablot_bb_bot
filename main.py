import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# מזהים מהסביבה
BOTLOG_CHANNEL = '@botlog_1221'  # הערוץ לפרסום
ADMIN_USERNAME = '@moishi_5104'  # מנהל לקבלת שם המשתמש

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message.text or "<הודעה ללא טקסט>"

    # פרסום בערוץ
    try:
        await context.bot.send_message(
            chat_id=BOTLOG_CHANNEL,
            text=f"📥 הודעה חדשה שהתקבלה:

{message}"
        )
    except Exception as e:
        print("שגיאה בשליחת הודעה לערוץ:", e)

    # שליחת שם המשתמש למנהל
    try:
        username = user.username or f"ID:{user.id}"
        await context.bot.send_message(
            chat_id=ADMIN_USERNAME,
            text=f"התקבלה הודעה מ: @{username}"
        )
    except Exception as e:
        print("שגיאה בשליחת שם משתמש למנהל:", e)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()
