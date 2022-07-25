# SPDX-FileCopyrightText: 2022 by Jessica E Calderon
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Mac Misc Shortcuts for Mac


from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode
from consumer import Toolbar

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'misc', # Application name
    'order': 0,
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x095E06, 'Open  ', [Keycode.COMMAND, 'o']),
        (0x544408, 'Save', [Keycode.COMMAND, 's']),
        (0x540908, 'Quit  ', [Keycode.COMMAND, 'q']),
        # 2nd row ----------
        (0x544408, 'All', [Keycode.COMMAND, 'a']),
        (0x544408, 'Copy', [Keycode.COMMAND, 'c']),
        (0x544408, 'Cut  ', [Keycode.COMMAND, 'x']),
        # 3rd row ----------
        (0x000000, '  ', []),
        (0x544408, 'Paste', [Keycode.COMMAND, 'p']),
        (0x000000, '  ', []),
        # 4th row ----------
        (0x080F54, '', []),
        (0x000000, '       ', []),
        (0x540908, 'Force Quit', [Keycode.COMMAND, Keycode.OPTION, Keycode.ESCAPE]),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
