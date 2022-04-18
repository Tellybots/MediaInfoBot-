# © @DKBOTZHELP Or https://github.com/DKBOTZHELP


import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "DK_BOTZ")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MediaInfosBot")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
