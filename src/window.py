import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from rename import *
from ui import *


class Main(QMainWindow, Ui_Rename):
    def __init__(self):
         super().__init__()
         self.setupUi(self)

         self.btn_folder.clicked.connect(self.select_folder)
         self.btn_clear.clicked.connect(self.clear_all)
         self.btn_confirm.clicked.connect(self.confirm_rename)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(None, "Select Folder")
        if len(folder) > 0:
            self.btn_clear.setEnabled(True)
            self.btn_confirm.setEnabled(True)
            self.text_folder.setText(f"{folder}")
            self.text_area.append(f"已選擇資料夾 {folder}")
            self.text_area.append("點擊 重新命名 按鈕來開始重新命名檔案...")
        else:
            self.text_area.append(f"請選擇資料夾...")

    def clear_all(self):
        self.btn_clear.setEnabled(False)
        self.btn_confirm.setEnabled(False)
        self.text_folder.setText("尚未選擇")
        self.text_area.append("重置完成 請選擇資料夾...")

    def confirm_rename(self):
        self.btn_folder.setEnabled(False)
        self.btn_clear.setEnabled(False)
        self.btn_confirm.setEnabled(False)
        folder = self.text_folder.text()
        self.text_area.append(f"開始對資料夾 {folder} 重新命名...")
        QApplication.processEvents()

        pdf_list = scan_pdf(folder)
        if len(pdf_list) == 0:
            self.text_area.append(f"目標資料夾 {folder} 沒有可以重新命名的檔案...")
            self.btn_folder.setEnabled(True)
            self.btn_clear.setEnabled(True)
            self.btn_confirm.setEnabled(True)
            QApplication.processEvents()
        else:
            count = 0
            error = 0
            success = 0
            for pdf in pdf_list:
                self.text_area.append(f"{pdf} 掃描條碼並重新命名中...")
                QApplication.processEvents()
                result = pdf_to_png(folder, pdf)
                if result is not None:
                    success += 1
                    self.text_area.append(f"{pdf} 重新命名為 {result}")
                    QApplication.processEvents()
                else:
                    error += 1
                    self.text_area.append(f"{pdf} 掃描不到條碼 重新命名失敗...")
                    QApplication.processEvents()
                count += 1
                self.text_area.append(f"已完成 {count} / {len(pdf_list)}")
                QApplication.processEvents()
            self.btn_folder.setEnabled(True)
            self.btn_clear.setEnabled(True)
            self.btn_confirm.setEnabled(True)
            self.text_area.append(f"重新命名完成 成功：{success} / 失敗：{error}")
            QApplication.processEvents()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
