from telethon import events
import asyncio

@borg.on(events.NewMessage(pattern=r"/.hi", outgoing=True))
async def hi(event):
    await event.reply("Hello")
