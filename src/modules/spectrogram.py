# # should contain old spectrogram code modified to work with the new classes

# # OLD FUNCTIONS
# # TODO: no idea make it work
from modules import emphasizer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from scipy import signal, mean
from scipy.io import wavfile
import os
import wave
import pylab


plt.rcParams['axes.facecolor'] = 'black'
plt.rc('axes', edgecolor='w')
plt.rc('xtick', color='w')
plt.rc('ytick', color='w')
plt.rcParams['savefig.facecolor'] = 'black'
plt.rcParams["figure.autolayout"] = True


def create_spectrogram_figure(self):
    self.figure = plt.figure()                     # Create matplotlib fig
    self.figure.patch.set_facecolor('black')
    self.axes = self.figure.add_subplot()
    self.Spectrogram = Canvas(self.figure)
    self.spectrogram_widget.addWidget(self.Spectrogram)


def plot_spectro(self):

    self.axes.clear()

    samples = self.music_signal.mastered_magnitude_array
    sample_rate = self.music_signal.f_sampling

    pylab.specgram(samples, Fs=sample_rate)
    self.Spectrogram.draw()
    self.figure.canvas.draw()
