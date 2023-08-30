import os
from pyshorteners import Shortener
from pyrogram import Client, filters

# ...

# Define your default shortener domain
DEFAULT_SHORTENER_DOMAIN = "pdisk.site"

# Define your other environment variables here

# ...

# Create your Client instance
dkbotz = Client(
    "Mdisk-Pro",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins={"root": "plugins"}
)

# Function to update the default shortener domain
def update_default_shortener_domain(new_domain):
    global DEFAULT_SHORTENER_DOMAIN
    DEFAULT_SHORTENER_DOMAIN = new_domain

# Handle the "/setdomain" command
@dkbotz.on_message(filters.command("setdomain"))
async def set_default_domain(_, message):
    if len(message.command) != 2:
        await message.reply("Usage: /setdomain [domain]")
        return

    new_domain = message.command[1]
    supported_domains = ["pdisk.site", "moneycase.link", "streaan.in/T/"]  # Add more if needed
    if new_domain in supported_domains:
        update_default_shortener_domain(new_domain)
        await message.reply(f"Default shortener domain set to {new_domain}")
    else:
        await message.reply("Invalid domain. Supported domains: " + ", ".join(supported_domains))

# ...

# Your start function and other bot logic here

# ...

# Run your bot
if __name__ == "__main__":
    dkbotz.run()
