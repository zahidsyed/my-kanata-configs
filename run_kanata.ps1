Stop-Process -Name "kanata" -ErrorAction SilentlyContinue

# Get the directory where this script is located
$dir = $PSScriptRoot

# Change directory to where this script is located
Set-Location $PSScriptRoot

# Use & (the call operator) for more reliable execution in Admin shells
& "$dir\kanata_windows_tty_winIOv2_cmd_allowed_x64.exe" --cfg "$dir\glove.eng.ara.kbd"