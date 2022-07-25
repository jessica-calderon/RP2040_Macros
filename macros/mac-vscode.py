# SPDX-FileCopyrightText: 2022 by Jessica E. Calderon
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: VSCode application for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode
from consumer import Toolbar

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Mac VSCode', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x6a0dad, 'Pref', [Keycode.SHIFT, Keycode.COMMAND, 'p']), # command palette
        (0x6a0dad, 'Open', [Keycode.COMMAND, 'o']), # open file
        (0x6a0dad, 'Settings', [Keycode.COMMAND, ',']), # open user settings
        # 2nd row ----------
        (0x009900, 'All', [Keycode.COMMAND, 'a']), # select all
        (0x009900, 'Copy', [Keycode.COMMAND, 'c']),
        (0x009900, 'Cut', [Keycode.COMMAND, 'x']),
        # 3rd row ----------
        (0xFFA500, 'Paste', [Keycode.COMMAND, 'v']),
        (0xFFA500, 'Comment', [Keycode.COMMAND, '/']), # toggle line comment on/off
        (0xFFA500, 'Format', [Keycode.SHIFT, Keycode.ALT, 'f']), # format code
        # 4th row ----------
        (0xb20000, 'Find All', [Keycode.SHIFT, Keycode.COMMAND, 'f']), # find in all docs
        (0xb20000, 'Find', [Keycode.COMMAND, 'f']), # find in doc
        (0xb20000, 'Terminal', [Keycode.SHIFT, Keycode.CONTROL, '`']), # open terminal
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
