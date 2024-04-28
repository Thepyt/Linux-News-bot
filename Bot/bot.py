import discord
import discord.ext
import os

import discord.ext.tasks

class Bot:
    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.message_content = True

        self.client = discord.Client(intents=self.intents)

    def message(self, message):
        @discord.ext.tasks.loop(count=1)
        async def autosend(channel):
            await channel.send(message[0])
            await channel.send(message[1])
    
        @self.client.event
        async def on_ready():
            if not autosend.is_running():
                channel_id = 0 # put the id here
                channel =  await self.client.fetch_channel(channel_id)
                autosend.start(channel)
            print("Ready")
        
        token = os.getenv("TOKEN")
        self.client.run(token)

