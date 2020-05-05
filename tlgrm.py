#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import os
import asyncio

try:
    from telethon import TelegramClient, eventsimport, connection
except ImportError:
		print("telethon module havn't been found. Use - pip3 install telethon")

api_id = os.environ['TELEGRAM_API_ID']
api_hash = os.environ['TELEGRAM_API_HASH']

# content of the automatic reply
message = '''Hey, I am a Bot 🤖 my owner is currently in an intense learning interval hiding in a cave.
          "He said, he will check his messages on Friday evening again.
          "In urgent cases, send him an SMS or even call him ☎ Sorry for the inconvenience: 😘'''

def main():
    # Create the client and connect
    client = TelegramClient('telehandler_session', api_id, api_hash)
    client.start()

    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        print(time.asctime(), '-', event.message)
        time.sleep(2)
        await event.reply(message)

    print(time.asctime(), '-', 'Waiting for incoming messages...')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')


if __name__ == '__main__':
    main()
else:
    sys.exit(os.EX_USAGE) # https://docs.python.org/2/library/os.html
