from meslib.Config import *
from meslib.Exceptions import *
import keyboard
import mouse
import time


class Inventory():
    def __init__(self, window, versionLevel, version):
        size = window.size
        self.version = version
        self.versionLevel = versionLevel
        self.INVSLOTS = {
                    "1": (size.height / 1.90, size.width/2.6),
                    "2": (size.height / 1.90, size.width/2.43),
                    "3": (size.height / 1.90, size.width/2.28),
                    "4": (size.height / 1.90, size.width/2.13),
                    "5": (size.height / 1.90, size.width/2.02),
                    "6": (size.height / 1.90, size.width/1.92),
                    "7": (size.height / 1.90, size.width/1.82),
                    "8": (size.height / 1.90, size.width/1.73),
                    "9": (size.height / 1.90, size.width/1.65),
                    "10": (size.height / 1.75, size.width / 2.6),
                    "11": (size.height / 1.75, size.width / 2.43),
                    "12": (size.height / 1.75, size.width / 2.28),
                    "13": (size.height / 1.75, size.width / 2.13),
                    "14": (size.height / 1.75, size.width / 2.02),
                    "15": (size.height / 1.75, size.width / 1.92),
                    "16": (size.height / 1.75, size.width / 1.82),
                    "17": (size.height / 1.75, size.width / 1.73),
                    "18": (size.height / 1.75, size.width / 1.65),
                    "19": (size.height / 1.60, size.width / 2.6),
                    "20": (size.height / 1.60, size.width / 2.43),
                    "21": (size.height / 1.60, size.width / 2.28),
                    "22": (size.height / 1.60, size.width / 2.13),
                    "23": (size.height / 1.60, size.width / 2.02),
                    "24": (size.height / 1.60, size.width / 1.92),
                    "25": (size.height / 1.60, size.width / 1.82),
                    "26": (size.height / 1.60, size.width / 1.73),
                    "27": (size.height / 1.60, size.width / 1.65),
                    "28": (size.height / 1.45, size.width / 2.6),
                    "29": (size.height / 1.45, size.width / 2.43),
                    "30": (size.height / 1.45, size.width / 2.28),
                    "31": (size.height / 1.45, size.width / 2.13),
                    "32": (size.height / 1.45, size.width / 2.02),
                    "33": (size.height / 1.45, size.width / 1.92),
                    "34": (size.height / 1.45, size.width / 1.82),
                    "35": (size.height / 1.45, size.width / 1.73),
                    "36": (size.height / 1.45, size.width / 1.65)
        }


        self.INVSLOTSDOUB = {
                    "1": (size.height / 1.65, size.width/2.6),
                    "2": (size.height / 1.65, size.width/2.43),
                    "3": (size.height / 1.65, size.width/2.28),
                    "4": (size.height / 1.65, size.width/2.13),
                    "5": (size.height / 1.65, size.width/2.02),
                    "6": (size.height / 1.65, size.width/1.92),
                    "7": (size.height / 1.65, size.width/1.82),
                    "8": (size.height / 1.65, size.width/1.73),
                    "9": (size.height / 1.65, size.width/1.65),
                    "10": (size.height / 1.50, size.width / 2.6),
                    "11": (size.height / 1.50, size.width / 2.43),
                    "12": (size.height / 1.50, size.width / 2.28),
                    "13": (size.height / 1.50, size.width / 2.13),
                    "14": (size.height / 1.50, size.width / 2.02),
                    "15": (size.height / 1.50, size.width / 1.92),
                    "16": (size.height / 1.50, size.width / 1.82),
                    "17": (size.height / 1.50, size.width / 1.73),
                    "18": (size.height / 1.50, size.width / 1.65),
                    "19": (size.height / 1.40, size.width / 2.6),
                    "20": (size.height / 1.40, size.width / 2.43),
                    "21": (size.height / 1.40, size.width / 2.28),
                    "22": (size.height / 1.40, size.width / 2.13),
                    "23": (size.height / 1.40, size.width / 2.02),
                    "24": (size.height / 1.40, size.width / 1.92),
                    "25": (size.height / 1.40, size.width / 1.82),
                    "26": (size.height / 1.40, size.width / 1.73),
                    "27": (size.height / 1.40, size.width / 1.65),
                    "28": (size.height / 1.30, size.width / 2.6),
                    "29": (size.height / 1.30, size.width / 2.43),
                    "30": (size.height / 1.30, size.width / 2.28),
                    "31": (size.height / 1.30, size.width / 2.13),
                    "32": (size.height / 1.30, size.width / 2.02),
                    "33": (size.height / 1.30, size.width / 1.92),
                    "34": (size.height / 1.30, size.width / 1.82),
                    "35": (size.height / 1.30, size.width / 1.73),
                    "36": (size.height / 1.30, size.width / 1.65)
        }


        self.ARMOR = {"1": (size.height / 3.2, size.width/2.6),
                      "2": (size.height / 2.8, size.width/2.6),
                      "3": (size.height / 2.4, size.width/2.6),
                      "4": (size.height / 2.15, size.width/2.6)}

        self.CRAFT = {"1": (size.height / 3, size.width/1.92),
                      "2": (size.height / 2.6, size.width/1.92),
                      "3": (size.height / 3, size.width/1.82),
                      "4": (size.height / 2.6, size.width/1.82),
                      "5": (size.height / 2.8, size.width/1.65)}

        self.SHIELD = {"1": (size.height / 2.15, size.width / 2.05)}

        self.BREWSTAND = {"1": (size.height / 2.35, size.width/2.2),
                          "2": (size.height / 2.2, size.width/2.03),
                          "3": (size.height / 2.35, size.width/1.9),
                          "4": (size.height / 3, size.width/2.5),
                          "5": (size.height / 3, size.width/2.03)}

        self.GRIND = {"1": (size.height / 2.55, size.width/2.25),
                      "2": (size.height / 3, size.width/2.25),
                      "3": (size.height / 2.6, size.width/1.75)}

        self.CART = {"1": (size.height / 3.1, size.width/2.55),
                     "2": (size.height / 2.3, size.width/2.55),
                     "3": (size.height / 2.5, size.width/1.68)}

        self.DROPPER = {"1": (size.height / 3, size.width/2.15),
                        "2": (size.height / 3, size.width/2.025),
                        "3": (size.height / 3, size.width/1.92),
                        "4": (size.height / 2.6, size.width/2.15),
                        "5": (size.height / 2.6, size.width/2.025),
                        "6": (size.height / 2.6, size.width/1.92),
                        "7": (size.height / 2.3, size.width/2.15),
                        "8": (size.height / 2.3, size.width/2.025),
                        "9": (size.height / 2.3, size.width/1.92)}

        self.ENCH8 = {"1": (size.height / 2.4, size.width/2.55),
                      "2": (size.height / 2.4, size.width/2.37),
                      "3": (size.height / 3.1, size.width/1.875),
                      "4": (size.height / 2.6, size.width/1.875),
                      "5": (size.height / 2.3, size.width/1.875)}

        self.ENCH7 = {"1": (size.height / 2.4, size.width / 2.45),
                      "2": (size.height / 3.1, size.width / 1.875),
                      "3": (size.height / 2.6, size.width / 1.875),
                      "4": (size.height / 2.3, size.width / 1.875)}

        self.FURNACE = {"1": (size.height / 3, size.width/2.19),
                        "2": (size.height / 2.3, size.width/2.19),
                        "3": (size.height / 2.6, size.width/1.82)}


        self.CRAFTINGTABLE = {"1": (size.height / 3, size.width/2.4),
                              "2": (size.height / 3, size.width/2.26),
                              "3": (size.height / 3, size.width/2.12),
                              "4": (size.height / 2.6, size.width/2.4),
                              "5": (size.height / 2.6, size.width/2.26),
                              "6": (size.height / 2.6, size.width/2.12),
                              "7": (size.height / 2.3, size.width/2.4),
                              "8": (size.height / 2.3, size.width/2.26),
                              "9": (size.height / 2.3, size.width/2.12),
                              "10": (size.height / 2.6, size.width/1.78)}

        self.ANVIL = {"1": (size.height / 2.4, size.width/2.43),
                      "2": (size.height / 2.4, size.width/2.05),
                      "3": (size.height / 2.4, size.width/1.73),
                      "4": (size.height / 3, size.width/1.73)}

        self.CHEST = {
                     "1": (size.height / 3, size.width/2.61),
                     "2": (size.height / 3, size.width/2.44),
                     "3": (size.height / 3, size.width/2.28),
                     "4": (size.height / 3, size.width/2.15),
                     "5": (size.height / 3, size.width/2.03),
                     "6": (size.height / 3, size.width/1.92),
                     "7": (size.height / 3, size.width/1.82),
                     "8": (size.height / 3, size.width/1.73),
                     "9": (size.height / 3, size.width/1.65),
                     "10": (size.height / 2.6, size.width/2.61),
                     "11": (size.height / 2.6, size.width/2.44),
                     "12": (size.height / 2.6, size.width/2.28),
                     "13": (size.height / 2.6, size.width/2.15),
                     "14": (size.height / 2.6, size.width/2.03),
                     "15": (size.height / 2.6, size.width/1.92),
                     "16": (size.height / 2.6, size.width/1.82),
                     "17": (size.height / 2.6, size.width/1.73),
                     "18": (size.height / 2.6, size.width/1.65),
                     "19": (size.height / 2.3, size.width/2.61),
                     "20": (size.height / 2.3, size.width/2.44),
                     "21": (size.height / 2.3, size.width/2.28),
                     "22": (size.height / 2.3, size.width/2.15),
                     "23": (size.height / 2.3, size.width/2.03),
                     "24": (size.height / 2.3, size.width/1.92),
                     "25": (size.height / 2.3, size.width/1.82),
                     "26": (size.height / 2.3, size.width/1.73),
                     "27": (size.height / 2.3, size.width/1.65)}

        self.DCHEST = {
           "1": (size.height / 4, size.width/2.62),
           "2": (size.height / 4, size.width/2.44),
           "3": (size.height / 4, size.width/2.28),
           "4": (size.height / 4, size.width/2.15),
           "5": (size.height / 4, size.width/2.03),
           "6": (size.height / 4, size.width/1.92),
           "7": (size.height / 4, size.width/1.82),
           "8": (size.height / 4, size.width/1.74),
           "9": (size.height / 4, size.width/1.66),
           "10": (size.height / 3.3, size.width/2.62),
           "11": (size.height / 3.3, size.width/2.44),
           "12": (size.height / 3.3, size.width/2.28),
           "13": (size.height / 3.3, size.width/2.15),
           "14": (size.height / 3.3, size.width/2.03),
           "15": (size.height / 3.3, size.width/1.92),
           "16": (size.height / 3.3, size.width/1.82),
           "17": (size.height / 3.3, size.width/1.74),
           "18": (size.height / 3.3, size.width/1.66),
           "19": (size.height / 2.8, size.width/2.62),
           "20": (size.height / 2.8, size.width/2.44),
           "21": (size.height / 2.8, size.width/2.28),
           "22": (size.height / 2.8, size.width/2.15),
           "23": (size.height / 2.8, size.width/2.03),
           "24": (size.height / 2.8, size.width/1.92),
           "25": (size.height / 2.8, size.width/1.82),
           "26": (size.height / 2.8, size.width/1.74),
           "27": (size.height / 2.8, size.width/1.66),
           "28": (size.height / 2.45, size.width/2.62),
           "29": (size.height / 2.45, size.width/2.44),
           "30": (size.height / 2.45, size.width/2.28),
           "31": (size.height / 2.45, size.width/2.15),
           "32": (size.height / 2.45, size.width/2.03),
           "33": (size.height / 2.45, size.width/1.92),
           "34": (size.height / 2.45, size.width/1.82),
           "35": (size.height / 2.45, size.width/1.74),
           "36": (size.height / 2.45, size.width/1.66),
           "37": (size.height / 2.2, size.width/2.62),
           "38": (size.height / 2.2, size.width/2.44),
           "39": (size.height / 2.2, size.width/2.28),
           "40": (size.height / 2.2, size.width/2.15),
           "41": (size.height / 2.2, size.width/2.03),
           "42": (size.height / 2.2, size.width/1.92),
           "43": (size.height / 2.2, size.width/1.82),
           "44": (size.height / 2.2, size.width/1.74),
           "45": (size.height / 2.2, size.width/1.66),
           "46": (size.height / 1.96, size.width/2.62),
           "47": (size.height / 1.96, size.width/2.44),
           "48": (size.height / 1.96, size.width/2.28),
           "49": (size.height / 1.96, size.width/2.15),
           "50": (size.height / 1.96, size.width/2.03),
           "51": (size.height / 1.96, size.width/1.92),
           "52": (size.height / 1.96, size.width/1.82),
           "53": (size.height / 1.96, size.width/1.74),
           "54": (size.height / 1.96, size.width/1.66)
        }


    def execute_slot(self, type, slot):
        try:
            parsed_slot = type[str(slot)]
            y = parsed_slot[0]
            x = parsed_slot[1]
            time.sleep(0.05)
            mouse.move(x=x, y=y)
        except:
            raise_error(SlotNotFound, f'Could not find the requested slot: {slot}.')


    def slot(self, invslot = None, doubleinv = None, armor = None, craft = None, shield = None, brewing_stand = None,
             grindstone = None, cartography = None, dropper = None, enchant = None, furnace = None, crafting_table = None,
             anvil = None, chest = None, doublechest = None, smithing_table = None, shulker = None, dispenser = None,
             blast_furnace = None, smoker = None):
        if doubleinv != None:
            self.execute_slot(self.INVSLOTSDOUB, doubleinv)
        elif invslot != None:
            self.execute_slot(self.INVSLOTS, invslot)
        elif armor != None:
            self.execute_slot(self.ARMOR, armor)
        elif craft != None:
            self.execute_slot(self.CRAFT, craft)
        elif shield != None and self.versionLevel >= 10:
            self.execute_slot(self.SHIELD, shield)
        elif brewing_stand != None:
            self.execute_slot(self.BREWSTAND, brewing_stand)
        elif grindstone != None and self.versionLevel >= 14:
            self.execute_slot(self.GRIND, grindstone)
        elif cartography != None and self.versionLevel >= 14:
            self.execute_slot(self.CART, cartography)
        elif dropper != None and self.versionLevel >= 6:
            self.execute_slot(self.DROPPER, dropper)
        elif enchant != None and self.versionLevel >= 7: #Not sure if its the best way to implement both enchantment tables but it'll do
            self.execute_slot(self.ENCH8, enchant)
        elif enchant != None and self.versionLevel >= 1:
            self.execute_slot(self.ENCH7, enchant)
        elif furnace != None:
            self.execute_slot(self.FURNACE, furnace)
        elif crafting_table != None:
            self.execute_slot(self.CRAFTINGTABLE, crafting_table)
        elif anvil != None and self.versionLevel >= 3:
            self.execute_slot(self.ANVIL, anvil)
        elif chest != None:
            self.execute_slot(self.CHEST, chest)
        elif doublechest != None:
            self.execute_slot(self.DCHEST, doublechest)
        elif smithing_table != None and smithing_table <= 3 and smithing_table >= 1: #from down here its just aliases, though the smithing table has a modification.
            self.execute_slot(self.ANVIL, smithing_table)
        elif shulker != None:
            self.execute_slot(self.CHEST, shulker)
        elif blast_furnace != None:
            self.execute_slot(self.FURNACE, blast_furnace)
        elif smoker != None:
            self.execute_slot(self.FURNACE, smoker)
        elif dispenser != None:
            self.execute_slot(self.DROPPER, dispenser)
        else:
            raise_error(InventorySlotNotFound, f'Unknown slot.')


    def hotbar(self, slot: int):
        arg = slot  # can't be arsed to change all the arg variables to slot
        if arg < 1 or arg > 9:
            raise_error(UnreachableHotbarSlot,
                        f'The minecraft hotbar has 9 slots, numbered from 1-9. Therefore, {arg} could not be reached.')
        else:
            try:
                arg = str(arg)
                hotbarslots = {"1": HOTBAR_SLOT_1,
                               "2": HOTBAR_SLOT_2,
                               "3": HOTBAR_SLOT_3,
                               "4": HOTBAR_SLOT_4,
                               "5": HOTBAR_SLOT_5,
                               "6": HOTBAR_SLOT_6,
                               "7": HOTBAR_SLOT_7,
                               "8": HOTBAR_SLOT_8,
                               "9": HOTBAR_SLOT_9}
                keyboard.press_and_release(hotbarslots[str(arg)])
                keyboard.press_and_release('backspace')
            except:
                raise_error(UnreachableHotbarSlot, f'Unreachable hotbar slot, "{arg}".')


    def drop(self, whole=False, amount: int = 1):
        if whole:
            keyboard.press(WHOLE_DROP)
            keyboard.press_and_release('backspace')
            time.sleep(0.01)
            keyboard.release(WHOLE_DROP)
        elif amount == 1:
            keyboard.press(DROP)
            keyboard.press_and_release('backspace')
            time.sleep(0.01)
            keyboard.release(DROP)
        else:
            if (amount > 1 and amount < 64):
                for i in range(amount):
                    keyboard.press(DROP)
                    keyboard.press_and_release('backspace')
                    time.sleep(0.01)
                    keyboard.release(DROP)
            else:
                raise_error(InvalidDropAmount,
                            f'Invalid drop amount. "{amount}" The minimal amount is 1 and the max is 64')


    def inv(self):
        keyboard.press_and_release(OPEN_INVENTORY)
        keyboard.press_and_release('backspace')


    def inventory(self):
        self.inv()


    def sendtohotbar(self, dest: int):
        parsed_arg = {"1": 28, "2": 29, "3": 30, "4": 31, "5": 32, "6": 33, "7": 34, "8": 35, "9": 36}
        try:
            dest = parsed_arg[str(dest)]
            self.hotbar(dest)
        except:
            raise_error(UnreachableHotbarSlot, f'Could not reach the specified slot.')


    def pickplace(self, relative=False):
        if relative:
            mouse.click(mouse.RIGHT)
        else:
            mouse.click(mouse.LEFT)


    def swap_to_offhand(self):
        if self.versionLevel >= 10:
            keyboard.press(SWAP_OFFHAND)
            keyboard.press_and_release('backspace')
            time.sleep(0.01)
            keyboard.release(SWAP_OFFHAND)
        else:
            raise_error(VersionError,
                        f'Offhand Swapping was only introduced in the 1.9 version of minecraft! Your current version, {self.version} does not support it!')