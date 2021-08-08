from meslib.Config import *
import keyboard
import time
import os

class Affirmation():
    def __init__(self, user, msg, id):
        self.author = user
        self.text = msg
        self.msg = f'{CHAR_BEFORE_NAME}{user}{CHAR_AFTER_NAME} {msg} '
        self.id = id


class Chat():

    def get_chathistory(self):
        with open(os.getenv("APPDATA") + "/.minecraft/logs/latest.log", "r") as lines:
            log = lines.readlines()
            return log


    def parse_chat_history(self, limit):
        if limit is None:
            limit = 50**50
        chat = self.get_chathistory()
        history = []
        parsed_history = []
        entries = []
        parsed_entries = []
        msg = ''
        for i in chat:
            entries.append(i.lstrip())
        for k in entries:
            if k.startswith('['):
                if msg != '':
                    parsed_entries.append(msg)
                    msg = k
                else:
                    msg += k
            else:
                msg += k
        if msg != '':
            parsed_entries.append(msg)
        for message in parsed_entries:
            if ']: [CHAT]' in message:
                msg = message.split(']: [CHAT]')[1]
                index = parsed_entries.index(message)
                history.append(f'{msg} |ID|{index}'.strip())
        for i in range(limit):
            history.reverse()
            idbase = history[0].split('|ID|')
            id = idbase[1].strip()
            base = idbase[0]
            codes = ['Â','§1', '§2', '§3', '§4', '§5', '§6', '§7', '§8', '§9',
                     '§a', '§b', '§c', '§d', '§e', '§f',
                     '§k', '§l', '§m', '§n', '§o', '§r']
            try:
                ' '.join(base).strip()
                for i in codes:
                    try:
                        base = base.split(i)
                        base = ''.join(base)
                    except:
                        continue
                if base.startswith(CHAR_BEFORE_NAME):
                    base = base.split(CHAR_BEFORE_NAME)[1]
                    base = base.split(CHAR_AFTER_NAME)
                    user = base[0]
                    base.pop(0)
                else:
                    user = None
                msg = ''.join(base).strip()
                history.pop(0)
                affirmation = Affirmation(user.strip(), msg.strip(), id.strip())
                parsed_history.append(affirmation)
                history.reverse()
            except:
                try:
                    msg = base.strip()
                    for i in codes:
                        try:
                            msg = msg.split(i)
                            msg = ''.join(msg)
                        except:
                            continue
                    affirmation = Affirmation(None, msg.strip(), id.strip())
                    parsed_history.append(affirmation)
                    history.pop(0)
                    continue
                except:
                    continue
        return parsed_history


    def getchat(self, limit: int = 20):
        if limit == 0:
            return None
        chat = self.parse_chat_history(limit)
        chat.reverse()
        if chat == []:
            return None
        if limit == 1:
            return chat[0]
        else:
            return chat


    def say(self, arg):
        keyboard.press_and_release(OPEN_CHAT)
        for i in range(256):
            keyboard.press_and_release('backspace')
        time.sleep(0.055)
        keyboard.write(arg, delay=0)
        time.sleep(0.055)
        keyboard.press_and_release('Return')