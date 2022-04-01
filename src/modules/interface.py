# OLD CODE.. REMOVE THIS COMMENT WHEN DONE MODIFYING


from PyQt5.QtWidgets import QTabWidget, QAction, QPushButton, QSlider, QComboBox, QLCDNumber, QStackedWidget, QStackedLayout, QWidget, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from modules import openfile, emphasizer, instruments, spectrogram
from modules.utility import print_debug

# interface globals


def init_connectors(self):

    self.keys = self.findChild(QWidget, "keys")
    self.halftones = self.findChild(QWidget, "halftones")
    self.groupBox_4 = self.findChild(QGroupBox, "groupBox_4")
    self.verticalLayout_4 = self.findChild(QVBoxLayout, "verticalLayout_4")
    self.horizontalLayout_10 = self.findChild(QHBoxLayout, "horizontalLayout_10")
    self.horizontalLayout = self.findChild(QHBoxLayout, "horizontalLayout")
    
    self.layout = QStackedLayout()
    
    self.groupBox_4.setLayout(self.layout)
    self.layout.addWidget(self.halftones)
    self.layout.addWidget(self.keys)
    self.layout.setStackingMode(1)
    self.verticalLayout_4.addLayout(self.layout)
    self.layout.setAlignment(Qt.AlignCenter)


    '''Initializes all event connectors and triggers'''

    ''' Menu Bar'''
    self.actionOpen = self.findChild(QAction, "actionOpen")
    self.actionOpen.triggered.connect(
        lambda: openfile.browse_window(self))

  #play button
    self.play_pushButton = self.findChild(QPushButton, "play_pushButton")
    self.play_pushButton.clicked.connect(
        lambda: emphasizer.play(self))
  #pause button  
    self.pause_pushButton = self.findChild(QPushButton, "pause_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: emphasizer.pause(self))
  #stop
    self.stop_pushButton = self.findChild(QPushButton, "stop_pushButton")
    self.stop_pushButton.clicked.connect(
        lambda: emphasizer.stop(self))
  #Initialize Qt Timer
    self.timer = QtCore.QTimer()
    self.timer.setInterval(50)  # Overflow timer
    self.timer.timeout.connect(lambda: emphasizer.waveform_update_plot(self))  # Event handler
  # piano keys
   #c  
    self.pause_pushButton = self.findChild(QPushButton, "C_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(0))
    #D
    self.pause_pushButton = self.findChild(QPushButton, "D_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(1))
    #E
    self.pause_pushButton = self.findChild(QPushButton, "E_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(2))
    #F
    self.pause_pushButton = self.findChild(QPushButton, "F_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(3))
    #G
    self.pause_pushButton = self.findChild(QPushButton, "G_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(4))
    #A
    self.pause_pushButton = self.findChild(QPushButton, "A_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(5))
    #B   
    self.pause_pushButton = self.findChild(QPushButton, "B_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(6))


    # self.WindowTabs = self.findChild(QTabWidget, "WindowTabs")

    # ''' Composer Tab'''

    # self.clearComposerButton = self.findChild(
    #     QPushButton, "clearComposerButton")
    # self.clearComposerButton.clicked.connect(
    #     lambda: print_debug("Not connected"))

    # self.addSineButton = self.findChild(QPushButton, "addSineButton")
    # self.addSineButton.clicked.connect(
    #     lambda: print_debug("Not connected"))
    # # self.addSineButton.clicked.connect(
    # #    lambda: composer.plotSinusoidal(self))

    # self.deleteSineButton = self.findChild(QPushButton, "deleteSineButton")
    # self.deleteSineButton.hide()
    # self.deleteSineButton.clicked.connect(
    #     lambda: print_debug("Not connected"))

    # # Creator Sliders and LCD

    # # Phase
    # self.phaseSlider = self.findChild(QSlider, "phaseSlider")
    # self.phaseSlider.valueChanged.connect(
    #     lambda: print_debug("Not connected"))

    # self.phaseLCD = self.findChild(QLCDNumber, "phaseLCD")
    # self.phaseSlider.valueChanged.connect(
    #     lambda: print_debug("Not connected"))

    # # Created signals combobox
    # self.signalsMenu = self.findChild(QComboBox, "signalsMenu")
    # self.signalsMenu.currentIndexChanged.connect(
    #     lambda: print_debug("Not connected"))
