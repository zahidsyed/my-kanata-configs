import sys
import os
import subprocess
import platform

def switch_layout(target):
    current_os = platform.system() # Detects 'Windows' or 'Linux'

    if current_os == "Windows":
        # Run your existing batch files for Windows 
        script = "set_ara.bat" if target == "arabic" else "set_eng.bat"
        subprocess.run(["cmd", "/c", script], shell=True)
        
    elif current_os == "Linux":
        # Ubuntu specific layout switching (Standard GNOME)
        # 0 is usually English, 1 is usually Arabic
        index = "1" if target == "arabic" else "0"
        subprocess.run(["gsettings", "set", "org.gnome.desktop.input-sources", "current", index])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        switch_layout(sys.argv[1])