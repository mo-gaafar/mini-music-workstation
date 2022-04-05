# define class and related functions

from signal import signal
from click import pass_context
from modules import spectrogram
from matplotlib.pyplot import magnitude_spectrum
from scipy.fft import rfftfreq, rfft, ifft, irfft
import numpy as np
import sounddevice as sd
from modules.utility import *
from modules import spectrogram as spectro
import PyQt5.QtCore
import pyqtgraph as pg
import pygame
from PyQt5.QtWidgets import QMessageBox
# TODO: implement master volume control (pyaudio?)
# TODO: implement start play stop functionality
# TODO: implement waveform drawing in pyqtgraph
# TODO: preserve phase information when modifying the magnitude??????


class MusicSignal():

    def __init__(self, filepath=0, time_array=[], magnitude_array=[], f_sampling=1, n_channel=0):
        self.INSTRUMENT_FREQRANGE_DICT = {
            "violin": [(1000, 24000)],
            "drums": [(10, 499)],
            "wind": [(500, 999)]
        }
        '''Contains instrument name and corresponding array of freq range tuples'''

        self.INSTRUMENT_MULTIPLIER_DICT = {
            "violin": 1,
            "drums": 1,
            "wind": 1
        }
        '''Contains instrument magnitude multipliers'''

        self.magnitude_array = magnitude_array
        self.f_sampling = f_sampling
        self.n_samples = f_sampling*len(time_array)
        self.filepath = filepath
        self.n_channel = n_channel
        self.last_slider_value = 100

        self.time_array = time_array
        self.min = 0
        self.max = 1

        self.original_magnitude_array = magnitude_array
        self.current_magnitude_array = magnitude_array
        self.mastered_magnitude_array = magnitude_array

        self.original_freq_magnitude_array = []
        self.freq_magnitude_array = []
        self.freq_phase_array = []
        self.freq_array = []
        if len(self.current_magnitude_array) > 0:
            self.fft_update()

        print_debug(self.f_sampling)

    def fft_update(self):
        '''Calculates the fft for the current magnitude array'''
        # done once to save processing time instead of twice for mag and angle

        self.freq_array = rfftfreq(
            len(self.current_magnitude_array),
            1/self.f_sampling)
        fft_coefficients = rfft(self.current_magnitude_array)
        self.freq_phase_array = np.angle(fft_coefficients)

        self.original_freq_magnitude_array = np.abs(fft_coefficients)
        self.freq_magnitude_array = np.abs(fft_coefficients)
        self.modify_master_volume(
            self.last_slider_value)  # update master volume

    def phase_preserved_inverse(self):
        '''Restores complex values using magnitude * e^(i theta)'''
        complex_coefficients = np.multiply(
            self.freq_magnitude_array, np.exp(np.multiply(1j, self.freq_phase_array)))
        self.current_magnitude_array = np.int16(
            irfft(complex_coefficients))

        self.modify_master_volume(
            self.last_slider_value)  # update master volume

    def set_instrument_factor(self, instrument, factor):
        self.INSTRUMENT_MULTIPLIER_DICT[instrument] = factor

    def reset_signal(self):
        '''Stores original signal back into current (same with fft) '''
        pass

    def emphasize_frequency_range(self, starting, ending, factor):
        '''multiplies the frequency range's magnitude by a factor '''
        for frequency in self.freq_array:
            if starting < frequency < ending:
                # converting from frequency to corresponding fftfreq index
                freq_sample_interval = len(self.freq_array)/(self.f_sampling/2)
                freq_index = round(freq_sample_interval * frequency)
                # maintains original freq array values to reduce cpu load
                self.freq_magnitude_array[freq_index] = self.original_freq_magnitude_array[freq_index] * factor

    def update_fourier_magnitudes(self):
        '''Updates the magnitude arrays with the dictionary values'''

        # supports multiple bands ;) + more efficient
        for instrument in self.INSTRUMENT_FREQRANGE_DICT:
            for range_array_tuple in self.INSTRUMENT_FREQRANGE_DICT[instrument]:
                self.emphasize_frequency_range(
                    int(range_array_tuple[0]),
                    int(range_array_tuple[1]),
                    self.INSTRUMENT_MULTIPLIER_DICT[instrument])

    def modify_master_volume(self, volume_slider_value=100):
        self.last_slider_value = volume_slider_value
        factor = volume_slider_value/100
        self.mastered_magnitude_array = np.int16(np.multiply(factor,
                                                             self.current_magnitude_array))
        self.max = max(np.abs(self.mastered_magnitude_array))


def return_master_volume(self):
    vol = mapRange(np.abs(
        self.music_signal.mastered_magnitude_array[self.pointsToAppend]), 0, self.music_signal.max, 0, 100)
    return int(2 * vol)


def waveform_update_plot(self):
    # print_debug("Refresh Plot")
    update_sample_interval = 10000
    time = self.music_signal.time_array[self.pointsToAppend:
                                        self.pointsToAppend+update_sample_interval]
    magnitude = self.music_signal.mastered_magnitude_array[
        self.pointsToAppend:self.pointsToAppend+update_sample_interval]

    self.pointsToAppend += update_sample_interval
    self.waveform_widget.clear()

    pen = pg.mkPen(color=(0, 200, 150), style=PyQt5.QtCore.Qt.DotLine)

    self.waveform_widget.plot(time, magnitude, pen=pen)
    self.waveform_widget.plotItem.setXRange(time[0], time[-1])


def play(self):
    if (self.toggle_play == 0):
        print_debug("Interval in ms: ")
        interval = 1000*10000/(self.music_signal.f_sampling)
        print_debug(interval)
        self.timer.setInterval(interval)
        self.timer.start()

        if len(self.music_signal.mastered_magnitude_array[self.pointsToAppend:]) == 0:
            QMessageBox.warning(
                self, 'NO SIGNAL ', 'You have to plot a signal first')

        self.sound_object = pygame.sndarray.make_sound(
            array=self.music_signal.mastered_magnitude_array[self.pointsToAppend:])
        self.sound_object.play()
        spectro.plot_spectro(self)
        self.toggle_play = 1
    else:
        pass


def pause(self):

    self.timer.stop()
    self.sound_object.stop()
    self.toggle_play = 0


def stop(self):
    self.sound_object.stop()
    self.timer.stop()
    self.pointsToAppend = 0
    waveform_update_plot(self)
    self.toggle_play = 0


def emphasize(self):
    if len(self.music_signal.mastered_magnitude_array[self.pointsToAppend:]) == 0:
        QMessageBox.warning(
            self, 'NO SIGNAL ', 'You have to plot a signal first')
    else:

        pause(self)

        # updates magnitudes in frequency domain based on slider values
        self.music_signal.update_fourier_magnitudes()
        # restores complex values using magnitude * e^(i theta)
        self.music_signal.phase_preserved_inverse()
        # multiplies the frequency range's magnitude by a factor
        # self.music_signal.modify_master_volume(self.music_signal.last_slider_value)
        spectro.plot_spectro(self)

        # play(self)
