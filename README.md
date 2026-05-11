# my-kanata-configs

Adds an Arabic layer on the Colemak-DH layout, on Win & Ubuntu. Used on the Glove80 with a TailorKey layout. Allows use of BHRM with the Arabic layer.

## Ubuntu instructions
Ensure layout 0 is English, 1 is Arabic

## Windows instructions
1. kanata_windows_tty_winIOv2_cmd_allowed_x64.exe > place in same folder as run_kanata.ps1
2. Regular powershell terminal > .\run_kanata.ps1
		
## Component and Role
my_layout.kbd	The "Brain": Handles the Colemak-DH logic and BHRM.

layout_bridge.py	The "Translator": Changes OS language settings based on platform.

set_ara.bat/sh	The "Actuators": OS-specific commands to actually change the input language.

## Naming scheme
keyboard.lang1.lang2

### keyboard
kinesis
glove
std

## Kinesis layout
See commit a36ffb6 for Kinesis. May not work.

