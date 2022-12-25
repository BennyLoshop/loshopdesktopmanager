import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import json
import settings_view


def click_success():
    save = True
    MainWindow.close()


if __name__ == '__main__':
    with open('settings.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    save = False
    print("1")
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = settings_view.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.SaveOrCanel.clicked.connect(click_success)
    OpenDesktopManager = ui.OpenDesktopManager.setChecked(data["OpenDesktopManager"])
    FileAble = ui.FileAble.setChecked(data["FileAble"])
    FileAuto = ui.FileAuto.setChecked(data["FileAuto"])
    FireDirInput = ui.FireDirInput.setText(data["FireDirInput"])
    SoftwareAble = ui.SoftwareAble.setChecked(data["SoftwareAble"])
    SoftwareAuto = ui.SoftwareAuto.setChecked(data["SoftwareAuto"])
    SoftwareDirInput = ui.SoftwareDirInput.setText(data["SoftwareDirInput"])
    MainWindow.show()

    if not app.exec_():
        if 1:
            OpenDesktopManager = ui.OpenDesktopManager.isChecked()
            FileAble = ui.FileAble.isChecked()
            FileAuto = ui.FileAuto.isChecked()
            FireDirInput = ui.FireDirInput.text()
            SoftwareAble = ui.SoftwareAble.isChecked()
            SoftwareAuto = ui.SoftwareAuto.isChecked()
            SoftwareDirInput = ui.SoftwareDirInput.text()
            data = {
                "OpenDesktopManager": OpenDesktopManager,
                "FileAble": FileAble,
                "FileAuto": FileAuto,
                "FireDirInput": FireDirInput,
                "SoftwareAble":SoftwareAble,
                "SoftwareAuto":SoftwareAuto,
                "SoftwareDirInput":SoftwareDirInput
            }
            with open('settings.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
