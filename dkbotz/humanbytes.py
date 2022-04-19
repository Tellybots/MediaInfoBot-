# © @DKBOTZHELP Or https://github.com/DKBOTZHELP

import math
import time
import asyncio
from typing import Union
from pyrogram.types import Message, CallbackQuery
from pyrogram.errors import FloodWait


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'
