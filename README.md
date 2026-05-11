# my-kanata-configs


## Naming scheme
os.keyboard.lang1.lang2

### OS
win - Windows
nix - Unix
wnx - Both

### keyboard
kinesis
glove
std

# Ubuntu instructions
Ensure layout 0 is English, 1 is Arabic

# Windows instructions
Use the kanata_windows_tty_winIOv2_cmd_allowed_x64.exe
		
# Component and Role
my_layout.kbd	The "Brain": Handles the Colemak-DH logic and BHRM.

layout_bridge.py	The "Translator": Changes OS language settings based on platform.

set_ara.bat/sh	The "Actuators": OS-specific commands to actually change the input language.
