# coding: utf-8
# Copyright 2020 - Alexandre Silva ©


from meslib.Inventory import *
from meslib.Chat import *
import keyboard
import mouse
import time
import pygetwindow

'''This library is meant to be used as a tool to create external scrips for minecraft. It is NOT a library for creating plugins or forge modifications, clients or datapacks.
Examples of external scripts would be, an AFK Grinder, Anti-AFK script, Auto-Walker etc. It's all up to you and your imagination! It does NOT connect to your game, but instead,
it simulates your movements in a way that reproduces ingame actions. The usage of this library may be against the rules of some Minecraft Servers. Use it at your own risk.'''

__author__ = 'Alexandre Silva'
__version__ = 1.0


def negative(number):
    if number >= 0:
        final_number = number * -1
        return final_number
    else:
        final_number = number * 1
        return final_number


class Minecraft(Chat, Inventory):
    def __init__(self, version: str):
        versions = {"ALPHA": -1, "BETA": 0, "1.0": 1, "1.1": 2, "1.2": 3, "1.3": 4, "1.4": 5, "1.5": 6,
                    "1.6": 7, "1.7": 8, "1.8": 9, "1.9": 10, "1.10": 11, "1.11": 12, "1.12": 13, "1.13": 13,
                    "1.14": 14, "1.15": 15, "1.16": 16}
        self.version = version
        self.versionLevel = versions[str(self.version)]
        if self.version in versions:
            try:
                minecraftWindows = pygetwindow.getWindowsWithTitle('Minecraft')
                for window in minecraftWindows:
                    if f'Minecraft {self.version}' in window.title:
                        window.activate()
                        time.sleep(0.05)
                        window.maximize()
                        keyboard.press_and_release('Escape')
                        super().__init__(window, self.versionLevel, self.version)
                        time.sleep(0.1)
                        break
                else:
                    raise_error(MinecraftClientNotFound, f"Couldn't find any {self.version} Minecraft Client launched.")
            except:
                raise_error(MinecraftClientNotFound, f"Couldn't find any {self.version} Minecraft Client launched.")
        else:
            raise_error(VersionError,
                        f'Minecraft version Error. "{self.version}". Please make the version down to their decimals, ex.: "1.0", or check if the version is supported! (Note that you can still use complex minecraft versions in your minecraft Client. However, you can\'t in the class.')


    def attack(self, times: int = 1, cooldown: float = 0.1):
        for i in range(times):
            mouse.click(ATTACK)
            time.sleep(cooldown)


    def destroy(self, times: int = 1, pressTime: float = 1, cooldown: float = 0.1):
        for i in range(times):
            mouse.press(ATTACK)
            time.sleep(pressTime)
            mouse.release(ATTACK)
            time.sleep(cooldown)


    def place(self, times=1, cooldown: float = 0.1):
        for i in range(times):
            mouse.click(USE)
            time.sleep(cooldown)


    def use(self, times: int = 1, pressTime: float = 0.1, cooldown: float = 0.1):
        for i in range(times):
            mouse.press(USE)
            time.sleep(pressTime)
            mouse.release(USE)
            time.sleep(cooldown)


    def walk(self, direction: str, blocks: int = 1, seconds: float = 0, sprint: bool = False):
        authorized_directions = {'fwd': MOVE_FORWARD, 'forward': MOVE_FORWARD, 'front': MOVE_FORWARD,
                                 'bwd': MOVE_BACKWARDS, 'backwards': MOVE_BACKWARDS, 'back': MOVE_BACKWARDS,
                                 'right': MOVE_RIGHT, 'left': MOVE_LEFT}
        if direction in authorized_directions:
            direction_variable = authorized_directions[str(direction)]
            if seconds != 0:
                if sprint is True:
                    keyboard.press(SPRINT)
                    keyboard.press_and_release('Backspace')
                    time.sleep(0.3)
                    keyboard.release(SPRINT)
                keyboard.press(direction_variable)
                keyboard.press_and_release('backspace')
                time.sleep(seconds)
                keyboard.release(direction_variable)
                keyboard.press_and_release('backspace')
            else:
                block_maths = blocks * 0.23164234422025
                if sprint is True:
                    keyboard.press(SPRINT)
                    keyboard.press_and_release('Backspace')
                    time.sleep(0.3)
                    keyboard.release(SPRINT)
                keyboard.press(direction_variable)
                keyboard.press_and_release('backspace')
                time.sleep(block_maths)
                keyboard.release(direction_variable)
        else:
            error_directions = ''
            for direct in authorized_directions:
                error_directions += f'"{direct}" '
            raise_error(MovementException,
                        f'Unknown direction "{direction}". Please choose one of the following directions: {error_directions}')


    def jump(self, direction: str = None, times: int = 1, cooldown: float = 0.1, sprint: bool = False):
        authorized_directions = {'fwd': MOVE_FORWARD, 'forward': MOVE_FORWARD, 'front': MOVE_FORWARD,
                                 'bwd': MOVE_BACKWARDS, 'backwards': MOVE_BACKWARDS, 'back': MOVE_BACKWARDS,
                                 'right': MOVE_RIGHT, 'left': MOVE_LEFT}
        if direction == None:
            for i in range(times):
                keyboard.press(JUMP)
                keyboard.press_and_release('backspace')
                time.sleep(0.4)
                keyboard.release(JUMP)
                time.sleep(cooldown)
        else:
            if direction in authorized_directions:
                if sprint is True:
                    keyboard.press(SPRINT)
                    keyboard.press_and_release('Backspace')
                    time.sleep(0.3)
                    keyboard.release(SPRINT)
                direction_variable = authorized_directions[str(direction)]
                keyboard.press(direction_variable)
                keyboard.press_and_release('backspace')
                for i in range(times):
                    keyboard.press(JUMP)
                    keyboard.press_and_release('backspace')
                    time.sleep(0.4)
                    keyboard.release(JUMP)
                    time.sleep(cooldown)
                keyboard.release(direction_variable)
            else:
                error_directions = ''
                for direct in authorized_directions:
                    error_directions += f'"{direct}" '
                raise_error(MovementException,
                            f'Unknown direction "{direction}". Please choose one of the following directions: {error_directions}')


    def hold_shift(self):
        keyboard.press(CROUCH)
        keyboard.press_and_release('backspace')


    def unshift(self):
        keyboard.release(CROUCH)


    def shift(self, times: int = 1, sneaktime: float = 0, cooldown: float = 0.01):
        for i in range(times):
            keyboard.press(CROUCH)
            keyboard.press_and_release('backspace')
            time.sleep(sneaktime)
            keyboard.release(CROUCH)
            time.sleep(cooldown)


    def goto_mc(self):
        minecraftWindows = pygetwindow.getWindowsWithTitle('Minecraft')
        for window in minecraftWindows:
            if f'Minecraft {self.version}' in window.title:
                window.activate()
                time.sleep(0.05)
                window.maximize()
                keyboard.press_and_release('Escape')
                time.sleep(0.1)
                break
            else:
                raise_error(MinecraftClientNotFound, f"Couldn't find any {self.version} Minecraft Client launched.")
        else:
            raise_error(MinecraftClientNotFound, f"Couldn't find any {self.version} Minecraft Client launched.")
