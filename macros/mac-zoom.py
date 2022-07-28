# SPDX-FileCopyrightText: 2022 Jessica E. Calderon
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Zoom application for Mac


from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode
from consumer import Toolbar

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Zoom', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x540908, 'Audio  ', [Keycode.COMMAND, Keycode.SHIFT, 'a']), # toggle mute
        (0x544408, 'Screen ', [Keycode.COMMAND, Keycode.SHIFT, 's']), # screen share
        (0x04541B, 'Video  ', [Keycode.COMMAND, Keycode.SHIFT, 'v']), # toggle video share
        # 2nd row ----------
        (0x000754, 'Control', [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, 'h']),
        (0x000000, '       ', []),
        (0x000754, 'Leave  ', [Keycode.COMMAND, 'w']),
        # 3rd row ----------
        (0x000000, '       ', []),
        (0x095E06, 'Play/Pause', [Toolbar(ConsumerControlCode.PLAY_PAUSE)]),
        (0x000000, '       ', []),
        # 4th row ----------
        (0x080F54, 'Vol-   ', [Toolbar(ConsumerControlCode.VOLUME_DECREMENT)]),
        (0x000000, '       ', []),
        (0x080F54, 'Vol+   ', [Toolbar(ConsumerControlCode.VOLUME_INCREMENT)]),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, ',']) # preferences
    ]
}
