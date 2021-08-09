# coding: utf-8

# Created at 14/07/2021
__license__ = "GNU General Public License v3.0"
__author__ = "Alexandre Silva // MrKelpy"
__copyright__ = "© Alexandre Silva 2021"


class Keybinds:

    def __init__(self):
        # General Controls
        self.ATTACK = "left"  # Mouse left click
        self.USE = "right"  # Mouse right click
        self.PICK = "middle"  # Mouse middle click
        self.DROP = "q"
        self.OFFHAND = "f"
        self.CHAT = "t"

        # Movement Controls
        self.WALK_FWD = "w"
        self.WALK_LEFT = "a"
        self.WALK_BWD = "s"
        self.WALK_RIGHT = "d"
        self.JUMP = "space"
        self.SPRINT = "ctrl"

        # Inventory
        self.INVENTORY = "e"
        self.HOTBAR_1 = "1"
        self.HOTBAR_2 = "2"
        self.HOTBAR_3 = "3"
        self.HOTBAR_4 = "4"
        self.HOTBAR_5 = "5"
        self.HOTBAR_6 = "6"
        self.HOTBAR_7 = "7"
        self.HOTBAR_8 = "8"
        self.HOTBAR_9 = "9"
        self.HOTBAR_SLOTS = [self.HOTBAR_1, self.HOTBAR_2, self.HOTBAR_3, self.HOTBAR_4, self.HOTBAR_5,
                      self.HOTBAR_6, self.HOTBAR_7, self.HOTBAR_8, self.HOTBAR_9]
