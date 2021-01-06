from telethon.sync import events


@client.on(events.NewMessage(pattern=r"/.hi", outgoing=True))
async def hi(event):
    await event.reply("Hello")
