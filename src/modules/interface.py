# OLD CODE.. REMOVE THIS COMMENT WHEN DONE MODIFYING

from PyQt5 import QtCore
from PyQt5.QtWidgets import QTabWidget, QAction, QPushButton, QSlider, QComboBox, QLCDNumber, QStackedWidget, QStackedLayout, QWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QDial, QLabel, QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from modules import openfile, emphasizer, instruments, spectrogram
from modules.utility import print_debug

# interface globals


def create_piano_layout(self):
    self.keys = self.findChild(QWidget, "keys")
    self.halftones = self.findChild(QWidget, "halftones")
    self.verticalLayout_4 = self.findChild(QVBoxLayout, "verticalLayout_4")

    self.layout = QStackedLayout()

    self.layout.addWidget(self.halftones)
    self.layout.addWidget(self.keys)
    self.layout.setStackingMode(1)
    self.verticalLayout_4.addLayout(self.layout)
    self.layout.setAlignment(Qt.AlignCenter)


def init_connectors(self):
    '''Initializes all event connectors and triggers'''

    ''' Menu Bar'''
    self.actionOpen = self.findChild(QAction, "actionOpen")
    self.actionOpen.triggered.connect(
        lambda: openfile.browse_window(self))

  # play button
    self.play_pushButton = self.findChild(QPushButton, "play_pushButton")
    self.play_pushButton.clicked.connect(
        lambda: emphasizer.play(self))
  # pause button
    self.pause_pushButton = self.findChild(QPushButton, "pause_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: emphasizer.pause(self))
  # stop
    self.stop_pushButton = self.findChild(QPushButton, "stop_pushButton")
    self.stop_pushButton.clicked.connect(
        lambda: emphasizer.stop(self))
  # Initialize Qt Timer
    self.timer = QtCore.QTimer()
    self.timer.setInterval(50)  # Overflow timer
    self.timer.timeout.connect(
        lambda: emphasizer.waveform_update_plot(self))  # Event handler

  ################### piano keys ##############################
   # c
    self.C_pushButton = self.findChild(QPushButton, "C_pushButton")
    self.C_pushButton.pressed.connect(
        lambda: self.guitar_instrument.ks())
    # c sharp
    self.Csharp_pushButton = self.findChild(QPushButton, "Csharp_pushButton")
    self.Csharp_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(1))
    # d
    self.D_pushButton = self.findChild(QPushButton, "D_pushButton")
    self.D_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(2))
    # d sharp
    self.pause_pushButton = self.findChild(QPushButton, "Dsharp_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(3))
    # e
    self.pause_pushButton = self.findChild(QPushButton, "E_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(4))
    # f
    self.pause_pushButton = self.findChild(QPushButton, "F_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(5))
    # f sharp
    self.pause_pushButton = self.findChild(QPushButton, "Fsharp_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(6))
    # g

    self.pause_pushButton = self.findChild(QPushButton, "G_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(7))
    # g sharp
    self.pause_pushButton = self.findChild(QPushButton, "Gsharp_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(8))
    # a
    self.pause_pushButton = self.findChild(QPushButton, "A_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(9))
    # a sharp
    self.pause_pushButton = self.findChild(QPushButton, "Asharp_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(10))
    # b
    self.pause_pushButton = self.findChild(QPushButton, "B_pushButton")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(11))

    self.pause_pushButton = self.findChild(QPushButton, "C_pushButton_2")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(12))

    self.pause_pushButton = self.findChild(QPushButton, "Csharp_pushButton_2")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(13))

    self.pause_pushButton = self.findChild(QPushButton, "D_pushButton_2")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(14))

    self.pause_pushButton = self.findChild(QPushButton, "Dsharp_pushButton_2")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(15))

    self.pause_pushButton = self.findChild(QPushButton, "E_pushButton_2")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(16))

    self.pause_pushButton = self.findChild(QPushButton, "F_pushButton_2")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(17))

    self.pause_pushButton = self.findChild(QPushButton, "Fsharp_pushButton_2")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(18))

    self.pause_pushButton = self.findChild(QPushButton, "G_pushButton_2")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(19))

    self.pause_pushButton = self.findChild(QPushButton, "Gsharp_pushButton_2")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(20))

    self.pause_pushButton = self.findChild(QPushButton, "A_pushButton_2")
    self.pause_pushButton.clicked.connect(
        lambda: self.piano_instrument.generating_note(21))

    self.Asharp_pushButton_2 = self.findChild(
        QPushButton, "Asharp_pushButton_2")
    self.Asharp_pushButton_2.clicked.connect(
        lambda: self.piano_instrument.generating_note(22))

    self.B_pushButton_2 = self.findChild(QPushButton, "B_pushButton_2")
    self.B_pushButton_2.clicked.connect(
        lambda: self.piano_instrument.generating_note(23))
    # DIAL 2
    self.octave_dial = self.findChild(QDial, "octave_dial")
    self.octave_dial.valueChanged.connect(
        lambda: self.piano_instrument.dial_value(self.octave_dial.value()))

    self.octave_lcd = self.findChild(QLCDNumber, "octave_lcd")
    self.octave_dial.valueChanged.connect(
        lambda: self.octave_lcd.display(self.octave_dial.value()))

    self.piano_volume_label = self.findChild(QLabel, "piano_volume_label")
    self.piano_volume_dial.valueChanged.connect(
        lambda: self.piano_volume_label.setText(str(self.piano_volume_dial.value())))

    #self.chord_lcd = self.findChild(QLCDNumber, "chord_lcd")
    #self.chord_lcd.display('a')

    ############################ Drums buttons ###################################

    self.snare_pushButton = self.findChild(QPushButton, "snare_pushButton")
    self.snare_pushButton.clicked.connect(
        lambda: self.drums_instrument.selecting_drum_kit('snare'))

    self.kick_pushButton = self.findChild(QPushButton, "kick_pushButton")
    self.kick_pushButton.clicked.connect(
        lambda: self.drums_instrument.selecting_drum_kit('kick'))

    self.kick_pushButton_3 = self.findChild(QPushButton, "kick_pushButton_3")
    self.kick_pushButton_3.clicked.connect(
        lambda: self.drums_instrument.selecting_drum_kit('kick'))

    self.highhat1_pushButton = self.findChild(
        QPushButton, "highhat1_pushButton")
    self.highhat1_pushButton.clicked.connect(
        lambda: self.drums_instrument.selecting_drum_kit('hat'))

    self.highhat_2pushButton = self.findChild(
        QPushButton, "highhat_2pushButton")
    self.highhat_2pushButton.clicked.connect(
        lambda: self.drums_instrument.selecting_drum_kit('hat'))

    self.hightom_pushButton = self.findChild(QPushButton, "hightom_pushButton")
    self.hightom_pushButton.clicked.connect(
        lambda: self.drums_instrument.selecting_drum_kit('H_tom'))

    self.floortom_pushButton = self.findChild(
        QPushButton, "floortom_pushButton")
    self.floortom_pushButton.clicked.connect(
        lambda: self.drums_instrument.selecting_drum_kit('FLoor_tom'))

    self.crash_pushButton = self.findChild(QPushButton, "crash_pushButton")
    self.crash_pushButton.clicked.connect(
        lambda: self.drums_instrument.selecting_drum_kit('crash_cymbal'))
    ################### guitar keys ##############################
    self.Estring_pushButton = self.findChild(QPushButton, "Estring_pushButton")
    self.Estring_pushButton.clicked.connect(
        lambda: self.guitar_instrument.guitar_string_sound(0))

    self.Astring_pushButton = self.findChild(QPushButton, "Astring_pushButton")
    self.Astring_pushButton.clicked.connect(
        lambda: self.guitar_instrument.guitar_string_sound(1))

    self.Dstring_pushButton = self.findChild(QPushButton, "Dstring_pushButton")
    self.Dstring_pushButton.clicked.connect(
        lambda: self.guitar_instrument.guitar_string_sound(2))

    self.Gstring_pushButton = self.findChild(QPushButton, "Gstring_pushButton")
    self.Gstring_pushButton.clicked.connect(
        lambda: self.guitar_instrument.guitar_string_sound(3))

    self.Bstring_pushButton = self.findChild(QPushButton, "Bstring_pushButton")
    self.Bstring_pushButton.clicked.connect(
        lambda: self.guitar_instrument.guitar_string_sound(4))

    self.Estring_pushButton_2 = self.findChild(QPushButton, "Estring_pushButton_2")
    self.Estring_pushButton_2.clicked.connect(
        lambda: self.guitar_instrument.guitar_string_sound(5))

    self.chord_dial = self.findChild(QDial, "chord_dial")
    self.chord_dial.valueChanged.connect(
        lambda: self.guitar_instrument.guitar_chord_selection(self.chord_dial.value()))

    self.chord_lcd = self.findChild(QLCDNumber, "chord_lcd")
    self.chord_dial.valueChanged.connect(
        lambda: self.chord_lcd.display(self.chord_dial.value()))
    

    # ++++++++++++++++++++EMPHASIZER++++++++++++++++++++++++++
    self.verticalSlider_4 = self.findChild(QSlider, "verticalSlider_4")
    self.verticalSlider_4.sliderReleased.connect(
        lambda: self.music_signal.modify_instrument("wind", self.verticalSlider_4.value()/5))

    self.slider3_label = self.findChild(QLabel, "slider3_label")
    self.verticalSlider_4.valueChanged.connect(
        lambda: self.slider3_label.setText(str(self.verticalSlider_4.value())))

    self.verticalSlider_3 = self.findChild(QSlider, "verticalSlider_3")
    self.verticalSlider_3.sliderReleased.connect(
        lambda: self.music_signal.modify_instrument("violin", self.verticalSlider_3.value()/5))

    self.slider2_label = self.findChild(QLabel, "slider2_label")
    self.verticalSlider_3.valueChanged.connect(
        lambda: self.slider2_label.setText(str(self.verticalSlider_3.value())))

    self.verticalSlider_2 = self.findChild(QSlider, "verticalSlider_2")
    self.verticalSlider_2.sliderReleased.connect(
        lambda: self.music_signal.modify_instrument("drums", self.verticalSlider_2.value()/5))

    self.slider1_label = self.findChild(QLabel, "slider1_label")
    self.verticalSlider_2.valueChanged.connect(
        lambda: self.slider1_label.setText(str(self.verticalSlider_2.value())))

    self.verticalSlider = self.findChild(QSlider, "verticalSlider")
    self.verticalSlider.sliderReleased.connect(
        lambda: self.music_signal.modify_master_volume(self.verticalSlider.value()))

    self.master_label = self.findChild(QLabel, "master_label")
    self.verticalSlider.valueChanged.connect(
        lambda: self.master_label.setText(str(self.verticalSlider.value())))

    self.ride_pushButton = self.findChild(QPushButton, "ride_pushButton")
    self.ride_pushButton.clicked.connect(
        lambda: self.drums_instrument.selecting_drum_kit('ride_cymbal'))

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
