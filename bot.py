import discord
import os
from keep_alive import keep_alive

client = discord.Client()
recieve_channels = [#CHANNELS TO PULL FROM]
send_channels = [#CHANNELS TO SEND TO]

#tells that bot is ready in console
@client.event
async def on_ready():
  for channel_id in send_channels:
    print ('{0.user} is now online'.format(client))

#bot receives a message and reposts in send channels
@client.event
async def on_message(ctx):
  if ctx.channel.id in recieve_channels:
    for channel_id in send_channels:
      channelx = client.get_channel(channel_id)
      await channelx.send(f"Ping from **{ctx.guild.name}**: {ctx.content}")

#starts the bot and the anti-sleep    
keep_alive()
client.run(os.getenv(#'TOKEN'))

