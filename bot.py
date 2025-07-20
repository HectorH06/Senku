import discord
import os
from openai import OpenAI
from dotenv import load_dotenv
from commands import ejecutar_comando, get_comandos

# Shhhh
load_dotenv(".secrets")
openai_api_key = os.getenv("OPENAI_API_KEY")
discord_token = os.getenv("DISCORD_TOKEN")

# Cliente de OpenAI
openai_client = OpenAI(api_key=openai_api_key)

# Cliente de Discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    contenido = message.content.strip()

    # OpenAI cobra 
    if contenido.startswith("!senku "):
        prompt = contenido[len("!senku "):]

        try:
            response = openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response.choices[0].message.content
            await message.channel.send(reply)

        except Exception as e:
            await message.channel.send(":x: Error: Se te acabó la feria :scream:. Dile al admin que le pague más a OpenAI :money_mouth:")
            print(f"Error con OpenAI: {e}")
        return

    # Otros comandos
    if contenido.startswith("!"):
        comando = contenido[1:].strip().lower()

        if comando == "comandos":
            await message.channel.send(f"📋 **Lista de comandos:**\n{get_comandos()}")
        else:
            respuesta = ejecutar_comando(comando)
            if respuesta:
                await message.channel.send(respuesta)
            else:
                await message.channel.send("No te entendí we")

# Cmon botsito
client.run(discord_token)
