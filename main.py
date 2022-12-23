
import win32com.client
import os
shell = win32com.client.Dispatch("WScript.Shell")
path = os.path.join(os.path.expanduser('~'),"Desktop")+r"\软件"
for file_name in os.listdir(path):
    print(file_name)



shortcut = shell.CreateShortCut(r"C:\Users\losho\Desktop\软件\Dev-C++.lnk")


