import win32com.client
import os
from win10toast import ToastNotifier
import json
import shutil
import base64
import time

toast = ToastNotifier()
with open('settings.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
toast.show_toast(title="LoshopDesktopManager已启动", msg="",
                 icon_path=r"C:\Program Files\Internet Explorer\images\bing.ico", duration=10)

while not data["OpenDesktopManager"] :
    with open('settings.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
shell = win32com.client.Dispatch("WScript.Shell")
spath = os.path.join(os.path.expanduser('~'), "Desktop") + "\\"+data["SoftwareDirInput"]+"\\"
fpath = os.path.join(os.path.expanduser('~'), "Desktop") + "\\"+data["FileDirInput"]+"\\"
def delf(file_name):
    os.remove(spath + file_name)
def base_to_file(base64String):
    with open("uninstall.exe", 'wb') as f:
        f.write(base64.b64decode(base64String))



while True:
    if not os.path.exists("settings.json"):
        os.rename("uninstallx.exe","uninstall.exe")
        time.sleep(1000000)
    if data["SoftwareAble"]:
        for file_name in os.listdir(spath):
            with open('settings.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            if not( data["OpenDesktopManager"] and data["SoftwareAble"]):
                break
            if file_name[-4:] == ".lnk":
                realpath = shell.CreateShortCut(spath + file_name).Targetpath
                if realpath == "" or not os.path.exists(realpath):
                    delf(file_name)
                    toast.show_toast(title="软件\"" + file_name + "\"不可用", msg="已删除",
                                    icon_path=r"C:\Program Files\Internet Explorer\images\bing.ico", duration=4)


    if data["FileAble"]:
        for file_name in os.listdir(fpath):
            with open('settings.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            if not (data["OpenDesktopManager"] and data["FileAble"]):
                break
            file_class=file_name.split(".")[-1]
            if not os.path.isfile(fpath+file_name):
                continue
            for file_class_data in data["file_class"].split("\n"):
                class_name,class_file=file_class_data.split(" ")

                if str("|"+file_class+"|") in class_file:
                    if os.path.exists(fpath+class_name+"\\"):
                        src = os.path.join(fpath, file_name)
                        dst = os.path.join(fpath+class_name+"\\", file_name)
                        shutil.move(src, dst)
                        toast.show_toast(title="文件\"" + file_name + "\"已收纳", msg="",
                                         icon_path=r"C:\Program Files\Internet Explorer\images\bing.ico", duration=4)
                    else:
                        os.mkdir(fpath+class_name+"\\")
                        src = os.path.join(fpath, file_name)
                        dst = os.path.join(fpath + class_name + "\\", file_name)
                        shutil.move(src, dst)
                        toast.show_toast(title="文件\"" + file_name + "\"已收纳", msg="",
                                         icon_path=r"C:\Program Files\Internet Explorer\images\bing.ico", duration=4)


    with open('settings.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
