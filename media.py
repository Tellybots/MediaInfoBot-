
import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from configs import Config
from pyromod import listen
from pyrogram import Client


def main():
    dkbotz = dict(root="dkbotz")
    app = Client("Media-info-Bot",
                 bot_token=Config.BOT_TOKEN,
                 api_id=Config.API_ID,
                 api_hash=Config.API_HASH,
                 plugins=dkbotz,
                 workers=100)

    app.run()


if __name__ == "__main__":
    main()
