# coding: utf-8

# Created at 30/03/2021
__license__ = "GNU General Public License v3.0"
__author__ = "Alexandre Silva // MrKelpy"
__copyright__ = "© Alexandre Silva 2021"

class Message:

    def __init__(self, *args):

        self.content = args[0]
        self.id = args[1]

