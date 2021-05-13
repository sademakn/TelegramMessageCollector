from dotenv import dotenv_values
from telethon import TelegramClient, events, sync
import argparse
from time import sleep


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
parser.add_argument(
    "--sleep-time",
    help="sleep duration between messages, to avoid rate limit, recommended more than 1 seconds",
    default=None,
    required=False,
)

args = parser.parse_args()

config = dotenv_values(".env")

test_channel_link = "test20210513"
client = TelegramClient("session_name", config["api_id"], config["api_hash"])
client.start()

for message in client.iter_messages(args.source_chat):
    client.forward_messages(entity=args.target_chat, messages=message)
client.send_message(args.target_chat, f"all messages coppied successfully")
