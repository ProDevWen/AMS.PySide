# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtWidgets import QMainWindow

from Views.Main_ui import Ui_Form


class MainWindow(QMainWindow, Ui_Form):
    """A window to show the books available"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
