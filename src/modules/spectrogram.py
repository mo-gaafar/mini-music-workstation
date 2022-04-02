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
import os, wave, pylab


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


def plot_spectro(self, path):

    create_spectrogram_figure(self)
    self.sample_rate, self.samples = wavfile.read(path)
    self.samples = mean(self.samples, axis = 1)
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % path)
    pylab.specgram(self.samples, Fs=self.sample_rate)