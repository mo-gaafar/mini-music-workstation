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

    key_index = piano_key_index_dict[piano_keyboard]
    button_name = ""

    if key_index < 12:
        button_name = piano_dict[key_index]+"_pushButton"
    elif 12 <= key_index < 24:
        button_name = piano_dict[key_index-12]+"_pushButton_2"
    if key_index < 24:
        self.button = self.findChild(QPushButton, button_name)
        self.button.animateClick(50)


def about_us(self):
    QMessageBox.about(
        self, ' About ', 'This is a musical instruments emphasizer and a digital audio workstation \nCreated by junior students from the faculty of Engineering, Cairo University, Systems and Biomedical Engineering department \n \nTeam members: \n-Mohammed Nasser \n-Abdullah Saeed \n-Zeyad Mansour \n-Mariam Khaled \n \nhttps://github.com/mo-gaafar/Mini_Music_Workstation.git')


def init_connectors(self):
    '''Initializes all event connectors and triggers'''

    self.selection_tabWidget = self.findChild(
        QTabWidget, "selection_tabWidget")
    self.selection_tabWidget.currentChanged.connect(
        lambda:  update_current_tab_index(self, self.selection_tabWidget.currentIndex()))

    ''' Menu Bar'''
    self.actionOpen = self.findChild(QAction, "actionOpen")
    self.actionOpen.triggered.connect(
        lambda: openfile.browse_window(self))

    self.actionAbout_us = self.findChild(QAction, "actionAbout_Us")
    self.actionAbout_us.triggered.connect(
        lambda: about_us(self))

   #######################################
    # function for push buttons connectors
    emphasizer_buttons =["play_pushButton", "pause_pushButton","stop_pushButton"]

   
    for index in emphasizer_buttons:
        self.pushButton = self.findChild(QPushButton,index)
        if index == "play_pushButton":
            self.pushButton.clicked.connect(lambda: emphasizer.play(self))
        elif index == "pause_pushButton":
            self.pushButton.clicked.connect(lambda: emphasizer.pause(self))
        elif index == "stop_pushButton":
            self.pushButton.clicked.connect(lambda: emphasizer.stop(self))
 
    # Initialize Qt Timer
    self.timer = QtCore.QTimer()
    self.timer.setInterval(50)  # Overflow timer
    self.timer.timeout.connect(
        lambda: emphasizer.waveform_update_plot(self))  # Event handler

    ################### piano keys ##############################
    piano_keys_dict={"C_pushButton":self.C_pushButton,"Csharp_pushButton":self.Csharp_pushButton,"D_pushButton":self.D_pushButton,"Dsharp_pushButton":self.Dsharp_pushButton,
                     "E_pushButton":self.E_pushButton,"F_pushButton":self.F_pushButton,"Fsharp_pushButton":self.Fsharp_pushButton,"G_pushButton":self.G_pushButton,"Gsharp_pushButton":self.Gsharp_pushButton,
                     "A_pushButton":self.A_pushButton,"Asharp_pushButton":self.Asharp_pushButton,"B_pushButton":self.B_pushButton,"C_pushButton_2":self.C_pushButton_2,"Csharp_pushButton_2":self.Csharp_pushButton_2,
                     "D_pushButton_2":self.D_pushButton_2,"Dsharp_pushButton_2":self.Dsharp_pushButton_2,"E_pushButton_2":self.E_pushButton_2,"F_pushButton_2":self.F_pushButton_2,"Fsharp_pushButton_2":self.Fsharp_pushButton_2,
                     "G_pushButton_2":self.G_pushButton_2,"Gsharp_pushButton_2":self.Gsharp_pushButton_2,"A_pushButton_2":self.A_pushButton_2,"Asharp_pushButton_2":self.Asharp_pushButton_2,"B_pushButton_2":self.B_pushButton_2}
    notes=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

    for note,index in enumerate(piano_keys_dict):
        piano_keys_dict[index] = self.findChild(QPushButton,index)
        print(piano_keys_dict[index])
        print(notes[note])
        piano_keys_dict[index].pressed.connect(lambda: self.piano_instrument.generating_note(notes[note]))
   
    # DIAL 2
    self.octave_dial = self.findChild(QDial, "octave_dial")
    self.octave_dial.valueChanged.connect(
        lambda: self.piano_instrument.dial_value(self.octave_dial.value()))

    self.sus_dial = self.findChild(QDial, "sus_dial")
    self.overtones_dial = self.findChild(QDial, "overtones_dial")
    self.sus_dial.valueChanged.connect(
        lambda: self.piano_instrument.alter_sus_overtones_values(self.sus_dial.value(), self.overtones_dial.value()))
    self.overtones_dial.valueChanged.connect(
        lambda: self.piano_instrument.alter_sus_overtones_values(self.sus_dial.value(), self.overtones_dial.value()))

    self.sus_label = self.findChild(QLabel, "sus_label")
    self.sus_dial.valueChanged.connect(
        lambda: self.sus_label.setText(str(self.sus_dial.value())))

    self.overtones_label = self.findChild(QLabel, "overtones_label")
    self.overtones_dial.valueChanged.connect(
        lambda: self.overtones_label.setText(str(self.overtones_dial.value())))

    self.octave_lcd = self.findChild(QLCDNumber, "octave_lcd")
    self.octave_dial.valueChanged.connect(
        lambda: self.octave_lcd.display(self.octave_dial.value()))

    self.piano_volume_label = self.findChild(QLabel, "piano_volume_label")
    self.piano_volume_dial.valueChanged.connect(
        lambda: self.piano_volume_label.setText(str(self.piano_volume_dial.value())))
    self.piano_volume_dial.valueChanged.connect(
        lambda: self.piano_instrument.set_volume(self.piano_volume_dial.value()))

    # self.chord_lcd = self.findChild(QLCDNumber, "chord_lcd")
    # self.chord_lcd.display('a')

    ############################ Drums buttons ###################################

    drums_tones_dict={"snare_pushButton":'snare',"kick_pushButton":'kick',"kick_pushButton_3":'kick',"highhat1_pushButton":'hat',
                     "highhat_2pushButton":'hat',"hightom_pushButton":'H_tom',"floortom_pushButton":'FLoor_tom',
                     "crash_pushButton":'crash_cymbal',"ride_pushButton":'ride_cymbal'}

    for index in drums_tones_dict:
        self.pushButton = self.findChild(QPushButton,index)
        self.pushButton.pressed.connect(lambda: self.drums_instrument.selecting_drum_kit(drums_tones_dict[index]))
    

    ################### guitar keys ##############################

    guitar_keys_dict={"Estring_pushButton":0,"Astring_pushButton":1,"Dstring_pushButton":2,"Gstring_pushButton":3,
                      "Bstring_pushButton":4,"Estring_pushButton_2":5}

  
    for index in guitar_keys_dict:
        self.pushButton = self.findChild(QPushButton,index)
        self.pushButton.pressed.connect(lambda: self.guitar_instrument.guitar_string_sound(guitar_keys_dict[index]))

   

    self.chord_dial = self.findChild(QDial, "chord_dial")
    self.chord_dial.valueChanged.connect(
        lambda: self.guitar_instrument.guitar_chord_selection(self.chord_dial.value()))

    self.chord_lcd = self.findChild(QLCDNumber, "chord_lcd")
    self.chord_dial.valueChanged.connect(
        lambda: self.chord_lcd.display(self.guitar_instrument.set_chord_lcd(self.chord_dial.value())))

    self.guitar_volume_label = self.findChild(QLabel, "guitar_volume_label")

    self.guitar_volume_dial = self.findChild(QDial, "guitar_volume_dial")
    self.guitar_volume_dial.valueChanged.connect(lambda:
                                                 self.guitar_volume_label.setText(str(self.guitar_volume_dial.value())))
    self.guitar_volume_dial.valueChanged.connect(lambda:
                                                 self.guitar_instrument.set_volume(self.guitar_volume_dial.value()))

    # ++++++++++++++++++++EMPHASIZER++++++++++++++++++++++++++

    self.verticalSlider_4 = self.findChild(QSlider, "verticalSlider_4")
    self.verticalSlider_4.sliderReleased.connect(
        lambda: self.music_signal.set_instrument_factor("violin", self.verticalSlider_4.value()/5))
    self.verticalSlider_4.sliderReleased.connect(
        lambda: spectrogram.plot_spectro(self))

    self.slider3_label = self.findChild(QLabel, "slider3_label")
    self.verticalSlider_4.valueChanged.connect(
        lambda: self.slider3_label.setText(str(self.verticalSlider_4.value())))

    self.verticalSlider_3 = self.findChild(QSlider, "verticalSlider_3")
    self.verticalSlider_3.sliderReleased.connect(
        lambda: self.music_signal.set_instrument_factor("wind", self.verticalSlider_3.value()/5))

    self.master_volume_bar = self.findChild(QProgressBar, "master_volume_bar")
    self.timer.timeout.connect(
        lambda: self.master_volume_bar.setValue(emphasizer.return_master_volume(self)))

    self.slider2_label = self.findChild(QLabel, "slider2_label")
    self.verticalSlider_3.valueChanged.connect(
        lambda: self.slider2_label.setText(str(self.verticalSlider_3.value())))

    self.verticalSlider_2 = self.findChild(QSlider, "verticalSlider_2")
    self.verticalSlider_2.sliderReleased.connect(
        lambda: self.music_signal.set_instrument_factor("drums", self.verticalSlider_2.value()/5))

    self.slider1_label = self.findChild(QLabel, "slider1_label")
    self.verticalSlider_2.valueChanged.connect(
        lambda: self.slider1_label.setText(str(self.verticalSlider_2.value())))

    self.verticalSlider = self.findChild(QSlider, "verticalSlider")

    self.verticalSlider.sliderReleased.connect(
        lambda: self.music_signal.modify_master_volume(self.verticalSlider.value()))

    self.master_label = self.findChild(QLabel, "master_label")
    self.verticalSlider.valueChanged.connect(
        lambda: self.master_label.setText(str(self.verticalSlider.value())))

    self.apply_pushButton = self.findChild(QPushButton, "apply_pushButton")
    self.apply_pushButton.clicked.connect(lambda: emphasizer.emphasize(self))

    # Time lcd

    time_lcd_buttons =["sec_lcd","cs_lcd","min_lcd"]
    
    for index in time_lcd_buttons:
        self.lcd = self.findChild(QLCDNumber,index)
        if index == "sec_lcd":
            self.timer.timeout.connect(lambda: self.lcd.display( math.floor(self.pointsToAppend/self.music_signal.f_sampling) % 60))
        elif index == "cs_lcd":
            self.timer.timeout.connect(lambda: self.lcd.display(math.floor(((self.pointsToAppend/self.music_signal.f_sampling) % 1) * 100)))
        elif index == "min_lcd":
            self.timer.timeout.connect(lambda: self.lcd.display(((self.pointsToAppend/self.music_signal.f_sampling) / 60) // 1))


    
