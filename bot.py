import os
import discord
from dotenv import load_dotenv
import responses

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user.name} (id: {client.user.id}) has connected to Discord!")

    @client.event
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f"Hi {member.name}, welcome to the server!"
        )

    @client.event
    async def on_message(message):
        if message.author.id == client.user.id:  # ignore messages from ourselves
            return

        username = str(message.author.name)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await  send_message(message, user_message, is_private=False)
        # if message.content.startswith("$hello"):
        #     await message.channel.send("Hi there!")
    client.run(TOKEN)

"""server = discord.utils.get(client.guilds, name=SERVER)
print(f"{client.user} is connected to the following server:\n"
      f"{server.name} (id: {server.id})")"""
