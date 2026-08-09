import discord
import requests

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Le bot {client.user} est connecté et communique avec FastAPI !')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Si l'utilisateur demande une analyse sur Discord
    if message.content.startswith('!analyser'):
        await message.channel.send('⏳ *Transmission de la requête au backend FastAPI et analyse par Ollama en cours...*')
        
        # Extraire la question après la commande
        question = message.content.replace('!analyser', '').strip()
        if not question:
            question = "Analyse l'état général des pods."

        try:
            # Le bot appelle ton API FastAPI (Étape 1 et 2 du diagramme)
            response = requests.post("http://127.0.0.1:8000/chat", json={"message": question})
            
            if response.status_code == 200:
                data = response.json()
                diagnostic = data.get("diagnostic")
                
                # Envoi de la réponse finale sur Discord (Étape 8)
                # Sécurité pour ne pas dépasser la limite de 2000 caractères de Discord
                if len(diagnostic) > 1900:
                    diagnostic = diagnostic[:1900] + "...\n*(Rapport abrégé)*"

                # Envoi de la réponse finale sur Discord (Étape 8)
                await message.channel.send(f"**Rapport Smart ChatOps :**\n{diagnostic}")
            else:
                await message.channel.send("❌ Erreur : Le backend FastAPI ne répond pas.")
                
        except Exception as e:
            await message.channel.send(f"❌ Impossible de joindre le serveur local : {e}")

# Ton token Discord

# Exemple de ce qu'il faut faire dans bot.py :
import os
TOKEN = os.getenv("DISCORD_TOKEN")


client.run(TOKEN)