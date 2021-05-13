from dotenv import dotenv_values
from telethon import TelegramClient, events, sync
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "--source-chat",
    help="source chat line or id",
    default=None,
)
parser.add_argument(
    "--target-chat",
    help="target chat line or id",
    default=None,
)
args = parser.parse_args()

config = dotenv_values(".env")

test_channel_link = "test20210513"
client = TelegramClient("session_name", config["api_id"], config["api_hash"])
client.start()
client.send_message(test_channel_link, "hello")
