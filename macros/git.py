# SPDX-FileCopyrightText: 2022 Jessica Calderon
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: git terminal commands

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'git', # Application name
        'order': 0,
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'add', ['git add .\n']),
        (0x004000, 'commit', ['git commit -m ']),
        (0x004000, 'push', ['git push origin ']),
        # 2nd row ----------
        (0xff0076, 'pull', ['git pull origin ']),        
        (0xff0076, 'main', ['main\n']),
        (0x004000, 'develop', ['develop\n']),
        # 3rd row ----------
        (0x0a0dd8, 'merge', ['git merge ']),
        (0x0a0dd8, 'checkout', ['git checkout ']),
        (0x0a0dd8, '-b', ['-b ']),
        # 4th row ----------
        (0xc70000, 'status', ['git status']),
        (0xc70000, 'branch', ['git branch']),
        (0xFFFF00,  'clone', ['git clone ']),
        # Encoder button ---
        (0x000000, '', [Keycode.ENTER]) # ENTER key
    ]
}
