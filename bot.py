from responses import professional_responses
import discord
from config import DISCORD_TOKEN
import bardAsk
import random


async def send_message(message, user_message, is_private):
    try:
        if is_private:
            await message.author.send(random.choice(professional_responses))
        else:
            await message.channel.send(random.choice(professional_responses))

        user_message = (
            "give me the response with less than 2000 chars and as short as short. if there are lits, list  them with numbers. not with bullets. and without images. "
            + user_message
        )
        response = bardAsk.askAnything(user_message)
        # response = responses.get_response(user_message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said {user_message} in {channel}")

        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)

        else:
            await send_message(message, user_message, is_private=False)

    client.run(DISCORD_TOKEN)
