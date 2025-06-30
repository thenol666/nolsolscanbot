from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ChecklistBot is online. Use /scan <CA> to begin.")

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /scan <CA>")
        return
    ca = context.args[0]
    # Placeholder logic – real logic will pull MC, LP, holders, etc.
    await update.message.reply_text(f"Scanned CA: {ca}\n(MCAP, LP, volume, holder logic here...)")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("scan", scan))
app.run_polling()