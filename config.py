
import os
#delcaring all static variables
class Config(object):

    DISCORD_TOKEN=os.environ['DISCORD_TOKEN']
    GOOGLE_API_KEY =os.environ['GOOGLE_API_KEY']
    CSE_ID =os.environ['CSE_ID']
    POSTGRES_URL=os.environ['DATABASE_URL']
    #POSTGRES_URL='postgresql://postgres:postgress@127.0.0.1:5432/discord'