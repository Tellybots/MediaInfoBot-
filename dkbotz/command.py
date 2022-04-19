from typing import List
from typing import Union
import os
from pyrogram import filters
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

other_filters = filters.group & ~filters.edited & ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded
)


def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
