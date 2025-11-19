
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import yt_dlp
import os
import asyncio

TOKEN = os.getenv("TOKEN")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()

    if not url.startswith("http"):
        await update.message.reply_text("ابعت لينك صالح 😅")
        return

    await update.message.reply_text("ثواني بنحمل الفيديو ⏳🔥")

    try:
        ydl_opts = {
            'outtmpl': 'video.mp4',
            'quiet': True,
            'format': 'mp4'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, ydl.download, [url])

        await update.message.reply_video(video=open("video.mp4", "rb"))

        os.remove("video.mp4")

    except Exception as e:
        await update.message.reply_text("في مشكلة… جرب لينك تاني 😂")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()
