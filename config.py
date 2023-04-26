# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "25479482"))
API_HASH = os.environ.get("API_HASH", "6ab604ff91a73fb91cc6526818e28ab1")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6098879851:AAEUxjzRMmq7TQ7kY4ha6NXDLZGuqfkqbd4")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5736579519")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Pdisk")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://devilbot:Rajbot@cluster0.ldrbggy.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5736579519")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append('5736579519")
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "1001249000599")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "PDiskPro_Updates") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
