from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "7714727163:AAHTPb-FdfJ01CN7Gigcvp0ZTKhF1UceQdIY"

async def protect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    text = update.message.text or ""

    # Xóa link
    if "http://" in text or "https://" in text:
        await update.message.delete()

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, protect))
app.run_polling()
