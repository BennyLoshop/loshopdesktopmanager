import ctypes
import sys
import easygui

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def admin_exe():
    if is_admin():
        subprocess.call("net stop loshop_desktop_manager", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
        subprocess.call("ldmluncher.exe uninstall", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
        easygui.msgbox("LoshopDesktopManager已成功完成卸载！","LoshopDesktopManager", "完成")
    else:
        if sys.version_info[0] == 3:
            easygui.msgbox("LoshopDesktopManager完成卸载需要管理员权限，请在接下来的UAC确认权限弹窗中点击确认！", "LoshopDesktopManager", "确认")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


if __name__ == '__main__':
    admin_exe()
