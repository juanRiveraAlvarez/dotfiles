import os
opciones = ["  Shutdown","󰜉  Restart","󰍃  Logout"]
i = input()
if i == opciones[0]:
    os.system("systemctl poweroff")
elif i == opciones[1]:
    os.system("systemctl reboot")
elif i == opciones[2]:
    os.system("qtile cmd-obj -o cmd -f shutdown")
    



