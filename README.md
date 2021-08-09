# PythMC 1.0
___
PythMC Is a Library currently composed of PythMC.Interactions and PythMC.Chat. Both of these packages aim to interact with the Minecraft Environment, although externally, to create scripts to hopefully be of use for Python Programmers in automating mundane Minecraft tasks. PythMC Is the successor of [MESLIB](https://github.com/MrKelpy/MESL) and [PyMChat](https://github.com/MrKelpy/PyMChat), combined. **Please note that PythMC and @MrKelpy are not in any way linked to Microsoft or Mojang Studios in any way.**

The documentation below will be divided into Assets, Chat and Interactions, explaining and detailing the usage of the library.

**Pull requests and issue raising are always welcome.**
___
## Assets
Inside the assets, you can find code shared by most usable packages inside the library. Two classes present in here, are the `Keybinds` and `Interactor` class; Both of them are used throughout the library, and have a major influence on its behaviour. Both can be configured.

### Keybinds
Defines the Keybinds that the code will use to perform actions in the Minecraft Environment. Any keybind can be altered by setting a property in either a `GameLink` or `ChatLink` class as another character. This works because both aforementioned classes inherit from `Interactor`, which inherits from `Keybinds`. Below is the the implementation for the class, showing all the default preset keybinds. These match the default keybinds in the game.
```python
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
```
### Interactor
Defines the interaction functions between the code and the Minecraft Client. This is the direct parent to all the usable classes and there isn't much that needs to be explained here. You can configure the name of the Client you're using, so it can fetch the desired Minecraft Window for the actions to be performed on through `self._window_searchname`. It is by default set to search for all Windows containing `"Minecraft"`.
___
## PythMC.Interactions
This package contains a class named `GameLink`. This class is used to  perform physical actions in Minecraft. All the interactions performed within this class are *indirect*, meaning that they perform actions as if it were a human, rather than actually "controlling" the client. Below is the documentation for any implementation of this class, in the form of commentative code examples.
```python
from pythmc import GameLink

client = GameLink()  # Initialises an instance of GameLink, to take control of the Minecraft Client.

# Attacks performing a left-click by default.
# Parameters: duration, double
# "duration" is for how long (in seconds) the attack/destroy button should be held down for.
# "double" is if the action performed should be a double-click, incase of the set key being a mouse button.
client.attack() or client.destroy()

# Uses a block, tool, or anything else in the inventory slot once, performing a right-click by default.
# Parameters: duration
# "duration" is for how long (in seconds) the use button should be held down for.
client.use() or client.click()

# Drops items performing a "q" by default.
# Parameters: stack
# "stack" is for whether the drop action should drop all the items in the slot rather than only one item at a time.
client.drop()

# Changes the active hotbar slot number to the specified slot.
# Parameters: slot_number
# "slot_number" is for the defined slot 1-9 to be selected according to the Keybinds.
client.hotbar(1)

# Opens the inventory performing an "e" by default.
# The extension for this function is under development.
client.inventory() or client.inv()

# Switches to the offhand.
client.offhand()

# Presses down the walk key for a specified direction, for x amount of blocks. Defaults to WASD.
# Parameters: jumping, sprint, direction, blocks
# "jumping" Toggles walk/sprint jumping.
# "sprint" does exactly what you think it does.
# "direction" takes in a string, either [fwd, bwd, left, up] for the direction of the movement.
# "blocks" is the amount of blocks to walk. Defining "up" and more than 1 block will have no effect. NOTE: Block definitions while flying are not accurate.
client.walk("fwd", blocks=5)
```
___
## PythMC.Chat
This package contains two classes, named `ChatLink` and `Message`. The former is able to interact with the in-game chat in real time, and the latter is a class to pack the returning values of functions within `ChatLink`. Below is the documentation for any implementation of this class, in the form of commentative code examples.
You can configure the `self.default_logs_path` property to change the location of your `latest.log` file, which is where the messages are gathered from.
```python
from pythmc import ChatLink

chat = ChatLink()  # Initialises an instance of ChatLink, to take control of the Minecraft Chat.

# Returns a list of messages from the in-game chat.
message_list = chat.get_history(limit=10)

# Check Output 1 to see how it looks!
for message in message_list:
  print(message.content)
  
# Sends a message to the chat using similar methods as in PythMC.Interactions
chat.send("This is a sample message!")
```

### Output 1
```js
[+] JohnRockefailure has joined
[+] Senseimasterman9 has joined
Welcome | Steve | Senseimasterman9 to the server!
<| Investor | *Blist> Welcom
<| Griffin | *Jay> W e l c o m e ! E n j o y y o u r s t a y a t S a f e S u r v i v a l
<| Event Staff | *Enelis> o-o <--- (This one is a dummy! -MrKelpy)
<| Griffin | *Jay> oof
<| Veteran | Parkemon20000> thats... not normal
[-] JohnRockefailure has left
<| Phoenix | *Kelp> Gn all
```

### Message
The `Message` class holds any returning values coming from `ChatLink`. It has two properties:

    1. Content (The message content)
    2. ID (An identifier used to distinguish between messages)
___
## Special Thanks to...
To [SafeSurvival](https://minecraft-server-list.com/server/291843/), for being the testing ground for this project.
To Shaztopia, SafeSurvival's Owner, for allowing me to test `PythMC.Chat` there.
___
## Planned Features and Patches
- [ ] Inventory browsing and selection  
- [ ] Camera turning
- [ ] Make walking while flying accurate

___
## Copyright and Author
© Alexandre Silva 2021
Discord: Alex_#6533
Email: alexandresilva.coding@gmail.com