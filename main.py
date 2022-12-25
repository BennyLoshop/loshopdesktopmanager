import win32com.client
import os
from win10toast import ToastNotifier
toast = ToastNotifier()


def delf(file_name):
    os.remove(path+file_name)

shell = win32com.client.Dispatch("WScript.Shell")
path = os.path.join(os.path.expanduser('~'),"Desktop")+"\软件\\"
while True:
    for file_name in os.listdir(path):
        if file_name[-4:]==".lnk":
            #print(path+file_name)
            realpath=shell.CreateShortCut(path+file_name).Targetpath
            #print(realpath)
            if realpath == "" or not os.path.exists(realpath):
                delf(file_name)
                toast.show_toast(title="软件\""+file_name+"\"不可用", msg="已删除",icon_path=r"C:\Program Files\Internet Explorer\images\bing.ico", duration=4)
