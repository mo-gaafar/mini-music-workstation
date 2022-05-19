# OLD CODE.. REMOVE THIS COMMENT WHEN DONE MODIFYING

from ctypes import util
from PyQt5 import QtCore
from PyQt5.QtWidgets import QTabWidget, QProgressBar, QMessageBox, QAction, QPushButton, QSlider, QComboBox, QLCDNumber, QStackedWidget, QStackedLayout, QWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QDial, QLabel, QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from modules import openfile, emphasizer, instruments, spectrogram
from modules.utility import print_debug, print_log
import math

# interface globals
# Keyboard shortcuts
piano_dict = {0: "C", 1: "Csharp", 2: "D", 3: "Dsharp",
              4: "E", 5: "F", 6: "Fsharp", 7: "G", 8: "Gsharp",
              9: "A", 10: "Asharp", 11: "B"}

piano_key_index_dict = {
    "q": 0, "1": 1, "w": 2, "2": 3, "e": 4, "r": 5, "3": 6, "t": 7, "4": 8, "y": 9, "5": 10, "u": 11,
    "i": 12, "6": 13, "o": 14, "7": 15, "p": 16, "[": 17, "8": 18, "]": 19, "9": 20, "\\": 21, "0": 22, "'": 23}

piano_index_button_dict = {}

# initializing dict
for index in range(24):
    button_name = ""
    if index < 12:
        button_name = piano_dict[index]+"_pushButton"
    elif 12 <= index < 24:
        button_name = piano_dict[index-12]+"_pushButton_2"
    piano_index_button_dict[index] = button_name

drums_key_dict = {'s': "snare", 'a': "snare", 'x': "kick", 'z': "kick",
                  'e': "hat", 'w': "hat", 'j': "FLoor_tom", 'y': "crash_cymbal",
                  'u': "ride_cymbal", 'g': "H_tom"}

guitar_key_string_index_dict = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5}

guitar_dial_chord_dict = {1: "G_major", 2: "D_major",
                          3: "C_major", 4: "E_major", 5: "A_major"}

# function for push buttons connectors


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


def update_current_tab_index(self, index):
    self.current_tab_index = index


def animate_pushbutton(self, piano_keyboard):

    if piano_keyboard in piano_key_index_dict:
        key_index = piano_key_index_dict[piano_keyboard]
        button_name = piano_index_button_dict[key_index]
        self.button = self.findChild(QPushButton, button_name)
        self.button.animateClick(50)


def about_us(self):
    QMessageBox.about(
        self, ' About ', 'This is a musical instruments emphasizer and a digital audio workstation \nCreated by junior students from the faculty of Engineering, Cairo University, Systems and Biomedical Engineering department \n \nTeam members: \n-Mohammed Nasser \n-Abdullah Saeed \n-Zeyad Mansour \n-Mariam Khaled \n \nhttps://github.com/mo-gaafar/Mini_Music_Workstation.git')


def init_connectors(self):
    '''Initializes all event connectors and triggers'''

    self.selection_tabWidget.currentChanged.connect(
        lambda:  update_current_tab_index(self, self.selection_tabWidget.currentIndex()))

    ''' Menu Bar'''
    self.actionOpen = self.findChild(QAction, "actionOpen")
    self.actionOpen.triggered.connect(
        lambda: openfile.browse_window(self))

    self.actionAbout_us = self.findChild(QAction, "actionAbout_Us")
    self.actionAbout_us.triggered.connect(
        lambda: about_us(self))

    self.play_pushButton.clicked.connect(lambda: emphasizer.play(self))
    self.pause_pushButton.clicked.connect(lambda: emphasizer.pause(self))
    self.stop_pushButton.clicked.connect(lambda: emphasizer.stop(self))

    # Initialize Qt Timer
    self.timer = QtCore.QTimer()
    self.timer.setInterval(50)  # Overflow timer
    self.timer.timeout.connect(
        lambda: emphasizer.waveform_update_plot(self))  # Event handler

    for key_index in piano_index_button_dict.keys():
        self.button = self.findChild(
            QPushButton, piano_index_button_dict[key_index])
        self.button.pressed.connect(
            lambda k=key_index: self.piano_instrument.generating_note(key_index=k))

    # DIAL 2
    self.octave_dial.valueChanged.connect(
        lambda: self.piano_instrument.dial_value(self.octave_dial.value()))

    self.sus_dial.valueChanged.connect(
        lambda: self.piano_instrument.alter_sus_overtones_values(self.sus_dial.value(), self.overtones_dial.value()))
    self.overtones_dial.valueChanged.connect(
        lambda: self.piano_instrument.alter_sus_overtones_values(self.sus_dial.value(), self.overtones_dial.value()))

    self.sus_dial.valueChanged.connect(
        lambda: self.sus_label.setText(str(self.sus_dial.value())))

    self.overtones_dial.valueChanged.connect(
        lambda: self.overtones_label.setText(str(self.overtones_dial.value())))

    self.octave_dial.valueChanged.connect(
        lambda: self.octave_lcd.display(self.octave_dial.value()))

    self.piano_volume_dial.valueChanged.connect(
        lambda: self.piano_volume_label.setText(str(self.piano_volume_dial.value())))
    self.piano_volume_dial.valueChanged.connect(
        lambda: self.piano_instrument.set_volume(self.piano_volume_dial.value()))

    ############################ Drums buttons ###################################

    drums_tones_dict = {"snare_pushButton": 'snare', "kick_pushButton": 'kick', "kick_pushButton_3": 'kick', "highhat1_pushButton": 'hat',
                        "highhat_2pushButton": 'hat', "hightom_pushButton": 'H_tom', "floortom_pushButton": 'FLoor_tom',
                        "crash_pushButton": 'crash_cymbal', "ride_pushButton": 'ride_cymbal'}

    for button in drums_tones_dict.keys():
        self.pushButton = self.findChild(QPushButton, button)
        self.pushButton.pressed.connect(
            lambda tone=drums_tones_dict[button]: self.drums_instrument.play_drums(tone=tone))

    ################### guitar keys ##############################

    guitar_keys_dict = {0: "Estring_pushButton", 1: "Astring_pushButton", 2: "Dstring_pushButton", 3: "Gstring_pushButton",
                        4: "Bstring_pushButton", 5: "Estring_pushButton_2"}

    for key in guitar_keys_dict.keys():
        self.pushButton = self.findChild(QPushButton, guitar_keys_dict[key])
        self.pushButton.pressed.connect(
            lambda s=key: self.guitar_instrument.guitar_string_sound(string_num=s))

    self.chord_dial.valueChanged.connect(
        lambda: self.guitar_instrument.guitar_chord_selection(self.chord_dial.value()))

    self.chord_dial.valueChanged.connect(
        lambda: self.chord_lcd.display(self.guitar_instrument.set_chord_lcd(self.chord_dial.value())))

    self.guitar_volume_dial.valueChanged.connect(lambda:
                                                 self.guitar_volume_label.setText(str(self.guitar_volume_dial.value())))
    self.guitar_volume_dial.valueChanged.connect(lambda:
                                                 self.guitar_instrument.set_volume(self.guitar_volume_dial.value()))

    # ++++++++++++++++++++EMPHASIZER++++++++++++++++++++++++++
    self.timer.timeout.connect(
        lambda: self.master_volume_bar.setValue(emphasizer.return_master_volume(self)))

    self.verticalSlider_4.sliderReleased.connect(
        lambda: self.music_signal.set_instrument_factor("violin", self.verticalSlider_4.value()/5))
    self.verticalSlider_4.sliderReleased.connect(
        lambda: spectrogram.plot_spectro(self))
    self.verticalSlider_4.valueChanged.connect(
        lambda: self.slider3_label.setText(str(self.verticalSlider_4.value())))

    self.verticalSlider_3.sliderReleased.connect(
        lambda: self.music_signal.set_instrument_factor("wind", self.verticalSlider_3.value()/5))
    self.verticalSlider_3.valueChanged.connect(
        lambda: self.slider2_label.setText(str(self.verticalSlider_3.value())))

    self.verticalSlider_2.sliderReleased.connect(
        lambda: self.music_signal.set_instrument_factor("drums", self.verticalSlider_2.value()/5))
    self.verticalSlider_2.valueChanged.connect(
        lambda: self.slider1_label.setText(str(self.verticalSlider_2.value())))

    self.verticalSlider.sliderReleased.connect(
        lambda: self.music_signal.modify_master_volume(self.verticalSlider.value()))
    self.verticalSlider.valueChanged.connect(
        lambda: self.master_label.setText(str(self.verticalSlider.value())))

    self.apply_pushButton.clicked.connect(lambda: emphasizer.emphasize(self))

    # Time lcd
    self.timer.timeout.connect(lambda: self.sec_lcd.display(
        math.floor(self.pointsToAppend/self.music_signal.f_sampling) % 60))
    self.timer.timeout.connect(lambda: self.cs_lcd.display(math.floor(
        ((self.pointsToAppend/self.music_signal.f_sampling) % 1) * 100)))
    self.timer.timeout.connect(lambda: self.min_lcd.display(
        ((self.pointsToAppend/self.music_signal.f_sampling) / 60) // 1))
