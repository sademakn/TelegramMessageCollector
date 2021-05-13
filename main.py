from dotenv import dotenv_values
from telethon import TelegramClient, events, sync

config = dotenv_values(".env")

test_channel_link = "test20210513"
client = TelegramClient("session_name", config["api_id"], config["api_hash"])
client.start()
client.send_message(test_channel_link, "hello")