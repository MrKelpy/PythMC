# coding: utf-8

# Created at 26/07/2021
__license__ = "GNU General Public License v3.0"
__author__ = "Alexandre Silva // MrKelpy"
__copyright__ = "© Alexandre Silva 2021"

# Builtin imports
import re
FLAGS = re.MULTILINE

# Local application imports
from Chat.message import Message

def parse_chat_messages(history: list, limit: int):

    """
    Parses out chat messages from latest.log
    :param history: The latest.log lines
    :param limit: The limit estabilished for returning
    :return: List of Message objects
    """
    requested_messages = list()
    counter = 0  # Initiates a counter used to count the amount of valid messages being returned
    for line in reversed(history):

        if counter == limit: break

        if not re.search("\[(.*(CHAT))\]", line, flags=FLAGS):  # Excludes all lines that are not chatlogs.
            continue

        # Parses out the message content from the line
        message = re.split("\[(.*(CHAT))\]", line, flags=FLAGS)[-1].strip()
        if not message: continue

        line_number = history.index(line) + 1

        requested_messages.append(Message(message, line_number))
        counter += 1

    if not requested_messages:
        return None
    return reversed(requested_messages)