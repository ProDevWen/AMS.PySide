import sys

from PySide6.QtWidgets import QApplication

from Views import Main
from Views.Main import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ams = MainWindow()
    ams.show()
    sys.exit(app.exec_())
