#OLD CODE... REMOVE THIS COMMENT WHEN DONE MODIFYING

#NEW FUNCITONALITY: SHOULD DEAL WITH MUSIC FILES
#TODO: import mp3 file
#TODO: create MusicSignal object with filepath, time,magnitude, sampling frequency information

# # converts file path to SampledSignal object
from winsound import PlaySound 
from PyQt5.QtWidgets import QFileDialog
import wfdb
import csv
import numpy
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
import app
from modules.utility import print_debug

# from main import MAX_SAMPLES
# import viewer
import sounddevice as sd
from modules.emphasizer import *

def browse_window(self):
    self.graph_empty = False
    self.filename = QFileDialog.getOpenFileName(
        None, 'open the signal file', './', filter="Raw Data(*.mp3 *.wav)")
    path = self.filename[0]
    print_debug("Selected path: " + path)
    open_file(self,path)
	#play the sound 
   
# shows the sound waves
def open_file(self,path):

	# reading the audio file
	raw = wave.open(path)
	
	# reads all the frames
	# -1 indicates all or max frames
	signal = raw.readframes(-1)
	
	signal = np.frombuffer(signal, dtype ="int16")
	
	# gets the frame rate
	f_rate = raw.getframerate()
    
	print_debug("frame")
	print_debug(f_rate)
	time = np.linspace(0, len(signal) / f_rate,num = len(signal))
	
	self.music_signal= MusicSignal(path,time,signal,2*f_rate) 
	
	






