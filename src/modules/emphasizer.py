# define class and related functions

from modules import spectrogram
from matplotlib.pyplot import magnitude_spectrum
from scipy.fft import fftfreq, fft
import numpy as np
import pyaudio

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

    def __init__(self, filepath, time_array, magnitude_array, f_sampling):

        self.f_sampling = f_sampling
        self.n_samples = f_sampling*len(time_array)
        self.filepath = filepath

        self.original_time_domain = [[time_array], [magnitude_array]]
        self.current_time_domain = [[time_array], [magnitude_array]]

        self.freq_domain = [[], []]

    def fft_update(self):
        self.freq_domain = [
            np.abs(fft(self.current_time_domain), self.n_samples)]

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
