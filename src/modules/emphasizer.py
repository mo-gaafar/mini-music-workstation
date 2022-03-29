# define class and related functions

from click import pass_context
from modules import spectrogram
from matplotlib.pyplot import magnitude_spectrum
from scipy.fft import fftfreq, fft
import numpy as np
import sounddevice as sd

from modules.utility import print_debug


# TODO: implement master volume control (pyaudio?)
# TODO: implement start play stop functionality
# TODO: implement waveform drawing in pyqtgraph
# TODO: preserve phase information when modifying the magnitude??????


class MusicSignal():
    instrument_freqrange_dict = {
        "violin": [(1, 0)],
        "guitar": [(1, 2), (3, 4)]
    }
    '''Contains instrument name and corresponding array of freq range tuples'''

    instrument_magnitude_multiplier_dict = {
        "violin": 1,
        "guitar": 1
    }
    '''Contains instrument magnitude multiplier'''
    
    def __init__(self, filepath=0, time_array=[], magnitude_array=[], f_sampling=1):

        self.magnitude_array=magnitude_array
        self.f_sampling = f_sampling
        self.n_samples = f_sampling*len(time_array)
        self.filepath = filepath

        self.original_time_array = time_array
        self.current_time_array = time_array
        self.original_magnitude_array = magnitude_array
        self.current_magnitude_array =  magnitude_array

        self.freq_domain = [[], []]
        print_debug(self.f_sampling)

    
    def fft_update(self):
        self.freq_domain = [
            np.abs(fft(self.current_magnitude_array), self.n_samples)]

    def inverse_fft(self):
        pass

    def restore_original(self):
        '''Stores original signal back into current (same with fft) '''
        pass

    def remove_frequency_range(self, starting, ending):
        pass

    def modify_instrument(self, instrument_dict, magnitude_multiplier):
        '''Should make use of all fft functions defined above'''
        pass

def waveform_update_plot(self):
    time = self.music_signal.current_time_array[self.pointsToAppend:self.pointsToAppend+10000]
    magnitude = self.music_signal.current_magnitude_array[self.pointsToAppend:self.pointsToAppend+10000]
    self.pointsToAppend += 10000
    self.waveform_widget.plot(time, magnitude)
    self.waveform_widget.plotItem.setXRange(time[0]-1.0,time[9999])


         

def play(self):
    self.timer.start()
    sd.play(self.music_signal.current_magnitude_array, self.music_signal.f_sampling)
   



def pause(self):
    self.timer.stop()
    sd.stop()
   # self.toggle_play=1