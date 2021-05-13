from dotenv import dotenv_values
from telethon import TelegramClient, events, sync

config = dict(dotenv_values(".env"))


client = TelegramClient("session_name", config.api_id, config.api_hash)
client.start()
