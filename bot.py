from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "7714727163:AAHTPb-FdfJ01CN7Gigcvp0ZTKhF1UceQdI"

async def anti_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text.lower()
        if "http://" in text or "https://" in text or "t.me/" in text:
            await update.message.delete()

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, anti_link))
    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
