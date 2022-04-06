import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content==('.roll 20'):
        for y in range(20):
            x=random.randint(1,20)
            await message.channel.send(x)
    if message.content==('.roll'):
        x=random.randint(1,20)
        await message.channel.send(x)

client.run('Nzk4NjU3MTEyMjI5NDEyODY0.X_4NZQ.TKtsVYxm7U2daose8wezXlSgXCI')