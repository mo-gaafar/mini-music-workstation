# https://namingconvention.org/python/ use the pythonic naming convention here (friendly reminder)

from PyQt5 import QtGui, QtWidgets, uic
import sys


import qt_material
import modules.interface


class MainWindow(QtWidgets.QMainWindow):
    ''' This is the PyQt5 GUI Main Window'''

    def __init__(self, *args, **kwargs):
        ''' Main window constructor'''

        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('./resources/MainWindow.ui', self)


        # set the title and icon
        self.setWindowIcon(QtGui.QIcon('./data/icons/icon.png'))
        self.setWindowTitle("Nyquist Theory Illustrator")


       # initialize arrays and variables



def main():

    app = QtWidgets.QApplication(sys.argv)
    qt_material.apply_stylesheet(app, theme='light_blue.xml')
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
