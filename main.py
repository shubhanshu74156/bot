from pyrogram import Client, filters

# Create a Pyrogram Client
api_id = 25460251
api_hash = "09ad6dbfd667ec7632e4825cf0cedb30"
bot_token = "6875004343:AAHLvQ0ByKmqt4KYIf3QlX6YsQMKxCe6UpE"

app = Client("ST2000", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define a function to handle the /start command
@app.on_message(filters.command("start"))
def start_command(client, message):
    # Send "Hello" as a response to the /start command
    message.reply_text("Hello!")

# Run the bot
app.run()
