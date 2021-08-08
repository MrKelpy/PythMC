# coding: utf-8

# Created at 31/07/2021
__license__ = "GNU General Public License v3.0"
__author__ = "Alexandre Silva // MrKelpy"
__copyright__ = "© Alexandre Silva 2021"

# Builtin imports
import time

# Third-Party imports
import pygetwindow
import mouse
import keyboard

# Local Application imports
from assets.exceptions import *
from .keybinds import Keybinds

class Interactor(Keybinds):

    """
    The Interactor Class parents all other classes and is an essential for their functioning.
    It declares the functions that activate the client and perform actions within it, and interacts
    with the client in a more primitive way.
    """

    def __init__(self):

        super().__init__()
        self._window_searchname = f"Minecraft".strip()
        self._window = None
        self.__help__ = f"https://github.com/MrKelpy/PyMC"


    def _get_minecraft_window(self):
        """
        Searches for a Minecraft Window, and returns it.
        :return: xWindow
        """

        # Checks if the MC window is currently active. Returns it if so
        if pygetwindow.getActiveWindowTitle().startswith(self._window_searchname):
            return pygetwindow.getActiveWindow()

        # Loops through all the windows and returns the MC one, based on their name.
        for window in pygetwindow.getAllWindows():
            if window.title.startswith(self._window_searchname):
                return window

        raise MinecraftWindowNotFoundError(f"\"{self._window_searchname}\" window was not found.")


    def activate_mc(self):
        """
        Activates the Minecraft Client window.
        :return:
        """

        self._window = self._get_minecraft_window()
        if (not self._window.isActive or not self._window.isMaximized) and self._window_searchname in self._window.title:

            self._window.activate()
            self._window.maximize()
            self._perform("ESC")

            time.sleep(0.05)  # A short delay to allow minecraft to load


    @staticmethod
    def _perform(action_key, duration: float = 0, double: bool = False):
        """
        ::param duration:: The duration of the action
        ::param double:: Whether, if, and only if, the action is a Mouse Action, it should be a double-click.

        Performs a mouse/keyboard action.

        An action is defined as a mouse/keyboard interaction between
        the program and the Minecraft Client - The differentiation
        between a keyboard and mouse action is done automatically.

        This is because, mouse interactions can only be left, right or middle.
        Any other mouse actions are not supported by PyMC

        :return: String
        """

        # Mouse Double-Clicking case
        if action_key.lower() in (mouse.LEFT, mouse.RIGHT, mouse.MIDDLE):

            if double:
                mouse.double_click(action_key)  # Double-Clicking case
            elif duration == 0:
                mouse.click(action_key)  # Mouse pressing case | No pressing
            else:  # Mouse pressing case | Duration pressing
                mouse.press(action_key)
                time.sleep(duration)
                mouse.release(action_key)

            return f"MOUSE EVENT - {action_key.upper()}"

        # Keyboard pressing case
        if duration == 0:
            keyboard.press_and_release(action_key)
        else:

            keyboard.press(action_key)
            time.sleep(duration)
            keyboard.release(action_key)

        return f"KEYBOARD action_key - {action_key.upper()}"