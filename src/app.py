# https://namingconvention.org/python/ use the pythonic naming convention here (friendly reminder)

from PyQt5 import QtGui, QtWidgets, uic
from modules import utility as util
from modules import interface 
from modules.emphasizer import *

import sys


import qt_material


class MainWindow(QtWidgets.QMainWindow):
    ''' This is the PyQt5 GUI Main Window'''

    def __init__(self, *args, **kwargs):
        ''' Main window constructor'''

        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('./resources/music_ws_mainwindow.ui', self)

        # set the title and icon
        self.setWindowIcon(QtGui.QIcon('./resources/icons/io.png'))
        self.setWindowTitle("Music Workstation")

        interface.init_connectors(self)
        # initialize arrays and variables
        self.toggle_play=0
        self.music_signal= MusicSignal()

def main():

    app = QtWidgets.QApplication(sys.argv)
    # qt_material.apply_stylesheet(app, theme='light_blue.xml')
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
