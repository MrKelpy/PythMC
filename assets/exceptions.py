# coding: utf-8

# Created at 30/03/2021
__license__ = "GNU General Public License v3.0"
__author__ = "Alexandre Silva // MrKelpy"
__copyright__ = "© Alexandre Silva 2021"

class LogsNotFoundError(BaseException):

    """
    Occurs when a file isn't present at the set destination for the logs file.
    """


class MinecraftWindowNotFoundError(BaseException):

    """
    Occurs when the Minecraft Window configured is not found upon trying to send a message.
    """