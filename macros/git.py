# SPDX-FileCopyrightText: 2022 Jessica Calderon
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: git terminal commands

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'git', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Add', ['git add .']),
        (0x004000, 'Commit', ['git commit -m ']),
        (0x004000, 'Push', ['git push ']),
        # 2nd row ----------
        (0xff0076, 'origin', ['origin ']),
        (0x004000, 'main', ['main']),
        (0xff0076, 'Pull', ['git pull ']),
        # 3rd row ----------
        (0x0a0dd8, 'Merge', ['git merge ']),
        (0x0a0dd8, 'Checkout', ['git checkout ']),
        (0x0a0dd8, '-b', ['-b ']),
        # 4th row ----------
        (0xc70000, 'Status', ['git status']),
        (0xc70000, 'Branch', ['git branch']),
        (0xFFFF00,  'Clone', ['git clone ']),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
