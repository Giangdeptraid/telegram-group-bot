from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "7714727163:AAHTPb-FdfJ01CN7Gigcvp0ZTKhF1UceQdI"

async def protect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    text = update.message.text or ""

    if "http://" in text or "https://" in text:
        await update.message.delete()

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, protect))
app.run_polling()
