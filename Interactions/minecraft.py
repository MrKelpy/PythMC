# encoding: utf-8

# Created at 12/07/2021
__license__ = "GNU General Public License v3.0"
__author__ = "Alexandre Silva // MrKelpy"
__copyright__ = "© Alexandre Silva 2021"


# Builtin imports
import os
import time

# Third Party imports
import keyboard

# Local Application Imports
from assets.essentials.interactor import Interactor


class Controller(Interactor):

    """
    Represents the Minecraft Client. All the interactions performed within this class are *indirect*,
    meaning that they perform actions as if it were a human, rather than actually "controlling" the client..
    """


    def __init__(self):

        super().__init__()
        self._default_mc_directory = os.path.join(os.getenv("APPDATA"), ".minecraft")
        self.gui_scale = 3


    def attack(self, duration: int = 0, double: bool = False):
        """
        Attacks once, performing a left-click by default.
        If the duration is set to anything other than 0, it acts as a destroying action.
        If double is set to True, it'll perform a doubleclick.

        The alias destroy should be used incase of duration arguments.
        :return:
        """

        self.activate_mc()
        self._perform(self.ATTACK, duration=duration, double=double)

    # Attack alias
    destroy = attack


    def use(self, duration: int = 0):
        """
        Uses a block, tool, or anything else in the inventory slot once, performing a right-click by default.
        If the duration is set to anything other than 0, it holds down the use key.
        :return:
        """

        self.activate_mc()
        self._perform(self.USE, duration=duration)

    # Use alias
    click = use


    def drop(self, stack: bool = False):
        """
        Drops an item, performing a "q" click by default.
        :param stack: Presses CTRL, in order to drop a whole stack.
        :return:
        """

        self.activate_mc()

        if stack:
            for i in range(64):
                self._perform(self.DROP)
            return

        self._perform(self.DROP)


    def hotbar(self, slot_number: int):
        """
        Changes the active hotbar slot number to the specified slot.
        Performs a 1-9 press by default
        :param slot_number:
        :return:
        """

        self.activate_mc()
        self._perform(self.HOTBAR_SLOTS[slot_number-1])


    def inventory(self):
        """
        Opens the inventory.
        Performs an "e" by default.
        :return:
        """

        self.activate_mc()
        self._perform(self.INVENTORY)
        time.sleep(0.05)

    # Inventory alias
    inv = inventory


    def offhand(self):
        """
        Switches the item to the offhand.
        Performs an "f" by default
        :return:
        """

        self.activate_mc()
        self._perform(self.OFFHAND)

    def walk(self, direction: str = "fwd", blocks: int = 1, sprint: bool = False, jumping: bool = False):
        """
        Presses down the walk key for a specified direction, for x amount of blocks. Defaults to WASD.
        A Minecraft Player takes 0.232s to walk 1 block, so that is the base of the calculations.

        :param jumping: Toggles walk/spring jumping.
        :param sprint: It does exactly what you think it does.
        :param direction: string: fwd, bwd, left, up
        :param blocks: The amount of blocks to walk
        :return:
        """

        self.activate_mc()

        if jumping: keyboard.press(self.JUMP)  # Starts jumping
        if sprint: keyboard.press(self.SPRINT); blocks -= 1.7  # Starts sprinting

        if direction == "fwd": self._perform(self.WALK_FWD, blocks*0.232)
        if direction == "bwd": self._perform(self.WALK_BWD, blocks * 0.232)
        if direction == "left": self._perform(self.WALK_LEFT, blocks * 0.232)
        if direction == "right": self._perform(self.WALK_RIGHT, blocks * 0.232)
        if direction == "up": self._perform(self.JUMP, blocks * 0.232)

        if sprint: keyboard.release(self.SPRINT)  # Stops sprinting
        if jumping: keyboard.release(self.JUMP)  # Stops jumping