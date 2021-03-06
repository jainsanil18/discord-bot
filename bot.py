import discord
import requests
from config import Config
from googleapiclient.discovery import build
from db import Base,engine
from user_history import UserHistory

discord_token = Config.DISCORD_TOKEN
client = discord.Client()
google_api_key=Config.GOOGLE_API_KEY
google_cse_id=Config.CSE_ID

#create the defined tables in the db
Base.metadata.create_all(engine)

#to retrieve google search results
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=google_api_key)
    res = service.cse().list(q=search_term, cx=Config.CSE_ID,num=5, **kwargs).execute()
    return res


#when a message is created in a discord server
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    else:
        #if a hi message appears from some user
        if message.content.startswith('hi'):
            msg = 'hey'
            await message.channel.send(msg)

        #  a users can  google search 
        elif message.content.startswith('!google '):
            search_query=message.content.replace('!google ','')
            print(search_query)
            #save search query in db
            UserHistory.add(search_query,message.author.id)
            result = google_search(search_query,google_api_key,google_cse_id)
            for item in result['items']:
                await message.channel.send(item['link'])

        # if user wants his recent search history w.r.t to some  string 
        elif  message.content.startswith('!recent '):
            history=message.content.replace('!recent ','')
            print(history)
            result=UserHistory.get_search_history(history,message.author.id)
            print(len(result))
            for item in result:
                await message.channel.send(item)
    
    return

# when the discord bot goes online
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    return

# to run the discord bot
client.run(discord_token)

