# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all bot files to the container
COPY . .

# Expose port (if needed, but Telegram bot odatda tashqi portni ishlatmaydi)
# EXPOSE 8000 (foydalanilmasa, olib tashlang)

# Set environment variables (agar kerak bo'lsa)
ENV BOT_TOKEN=BOT_TOKEN

# Command to run the bot
CMD ["python", "bot.py"]