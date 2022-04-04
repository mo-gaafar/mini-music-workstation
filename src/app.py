# https://namingconvention.org/python/ use the pythonic naming convention here (friendly reminder)

from PyQt5 import QtGui, QtWidgets, uic, QtCore
from modules import utility as util
from modules import interface, resource
from modules.instruments import *
from modules.emphasizer import *

import sys

from modules.spectrogram import create_spectrogram_figure


class MainWindow(QtWidgets.QMainWindow):
    ''' This is the PyQt5 GUI Main Window'''

    def __init__(self, *args, **kwargs):
        ''' Main window constructor'''

        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('./resources/music_ws_mainwindow.ui', self)

        # set the title and icon
        self.setWindowIcon(QtGui.QIcon('./resources/icons/icon.png'))
        self.setWindowTitle("Music Workstation")

        print_debug("Connectors Initialized")

        # initialize arrays and variables
        #pygame.mixer.init()   
        pygame.mixer.pre_init( channels = 1, allowedchanges=0)
        pygame.mixer.init()

        self.music_signal = MusicSignal()
        self.piano_instrument= Piano()
        self.drums_instrument= Drums()
        self.guitar_instrument= Guitar()
        # initialize points to app
        self.pointsToAppend = 0
        interface.create_piano_layout(self)
        interface.init_connectors(self)
        create_spectrogram_figure(self)


def main():

    app = QtWidgets.QApplication(sys.argv)
    # qt_material.apply_stylesheet(app, theme='light_blue.xml')
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
