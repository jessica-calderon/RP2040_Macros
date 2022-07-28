# SPDX-FileCopyrightText: 2022 by Jessica E. Calderon
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Chrome web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Mac Chrome',  # Application name
    'macros': [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.COMMAND, '[']),
        (0x004000, 'Fwd >', [Keycode.COMMAND, ']']),
        (0x400000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x202000, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x202000, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),
        (0x400000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Reload', [Keycode.COMMAND, 'r']),
        (0x000040, 'Home', [Keycode.COMMAND, 'H']),
        (0x000040, 'Private', [Keycode.COMMAND, Keycode.SHIFT, 'N']),
        # 4th row ---------- # can configure to custom websites
        (0x000000, 'Google', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                            'https://google.com\n']),   # Google in new window
        (0x800000, 'Github', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                              'www.github.com\n']),   # Github in new window
        (0x101010, 'local', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                             'http://localhost:3001/\n']),  # localhost in new window
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w'])  # Close window/tab
    ]
}
