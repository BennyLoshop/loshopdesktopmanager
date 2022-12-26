import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import json
import settings_view
save = False

def click_success():
    save = True
    MainWindow.close()


if __name__ == '__main__':
    with open('settings.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    save = False
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = settings_view.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.SaveOrCanel.clicked.connect(click_success)
    OpenDesktopManager = ui.OpenDesktopManager.setChecked(data["OpenDesktopManager"])
    FileAble = ui.FileAble.setChecked(data["FileAble"])
    FileAuto = ui.FileAuto.setChecked(data["FileAuto"])
    FileDirInput = ui.FileDirInput.setText(data["FileDirInput"])
    SoftwareAble = ui.SoftwareAble.setChecked(data["SoftwareAble"])
    SoftwareAuto = ui.SoftwareAuto.setChecked(data["SoftwareAuto"])
    SoftwareDirInput = ui.SoftwareDirInput.setText(data["SoftwareDirInput"])
    file_class=ui.FileClass.setPlainText(data["file_class"])
    MainWindow.show()

    if not app.exec_():
        if 1:
            OpenDesktopManager = ui.OpenDesktopManager.isChecked()
            FileAble = ui.FileAble.isChecked()
            FileAuto = ui.FileAuto.isChecked()
            FileDirInput = ui.FileDirInput.text()
            SoftwareAble = ui.SoftwareAble.isChecked()
            SoftwareAuto = ui.SoftwareAuto.isChecked()
            SoftwareDirInput = ui.SoftwareDirInput.text()
            file_class = ui.FileClass.toPlainText()
            data = {
                "OpenDesktopManager": OpenDesktopManager,
                "FileAble": FileAble,
                "FileAuto": FileAuto,
                "FileDirInput": FileDirInput,
                "SoftwareAble":SoftwareAble,
                "SoftwareAuto":SoftwareAuto,
                "SoftwareDirInput":SoftwareDirInput,
                "file_class":file_class
            }
            with open('settings.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
