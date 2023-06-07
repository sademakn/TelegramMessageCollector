from dotenv import dotenv_values
from telethon import TelegramClient, events, sync, errors
import argparse
from time import sleep
from tqdm import tqdm

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
try:
    api_id = config["api_id"]
    api_hash = config["api_hash"]
except KeyError as e:
    print(e)
    raise Exception("you need to create a .env file containing api_id and api_hash, read the readme.md file")
client = TelegramClient("session_name", config["api_id"], config["api_hash"])
client.start()


target_chat = client.get_entity(args.target_chat)
tq = tqdm()

offset_id = 0
while True:
    for message in client.iter_messages(args.source_chat, reverse=True, offset_id=offset_id):
        try:
            client.forward_messages(entity=target_chat, messages=message)
        except errors.FloodWaitError as e:
            print('flood for', e.seconds)
        except Exception as e:
            print(e)
            continue
        tq.update(1)
        if args.sleep_time:
            sleep(float(args.sleep_time))
        offset_id = message.id
client.send_message(args.target_chat, f"all messages coppied successfully")
