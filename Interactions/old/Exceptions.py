class MovementException(Exception):
    pass


class UnreachableHotbarSlot(Exception):
    pass


class VersionError(Exception):
    pass


class VersionNotSupported(Exception):
    pass


class MinecraftClientNotFound(Exception):
    pass


class InventorySlotNotFound(Exception):
    pass


class InvalidDropAmount(Exception):
    pass


class SlotNotFound(Exception):
    pass


def error():
    raise ValueError('Error')


def raise_error(Error, msg):
    try:
        error()
    except ValueError as exc:
        raise Error(msg) from exc
