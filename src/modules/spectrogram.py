# # should contain old spectrogram code modified to work with the new classes

# # OLD FUNCTIONS
# # TODO: no idea make it work
from modules import emphasizer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from scipy import signal


def create_spectrogram_figure(self):
    self.figure = plt.figure()                     # Create matplotlib fig
    self.figure.patch.set_facecolor('black')
    self.axes = self.figure.add_subplot()
    self.spectrogram_widget = Canvas(self.figure)
    # self.spectrogram_widget.addWidget(self.Spectrogram)


def plot_spectro(self):

    # Clear spectrogram before plotting
    self.spectrogram_widget.draw()
    self.figure.canvas.draw()

    # Corner Case Of Empty Channel
    if len(self.music_signal.current_magnitude_array) == 0:
        self.axes.clear()
        self.spectrogram_widget.draw()
        self.figure.canvas.draw()

    else:
        if self.music_signal.f_sampling != 1:
            FS = self.music_signal.f_sampling

            self.freq, self.time, self.Sxx = signal.spectrogram(
                np.array(self.music_signal.current_magnitude_array),
                fs=self.music_signal.f_sampling,
                window='hanning',
                nperseg=128,
                noverlap=64,
                detrend=False,
                mode='magnitude',
                scaling='density')

            self.max_freq = np.max(self.freq)
            self.axes.set_ylim([0, self.max_freq])

            # Slices freq arr into range specified by sliders
            self.freqRange = np.where((self.freq >= 0)
                                      & (self.freq <= 10000))
            self.freq = self.freq[self.freqRange]
            self.Sxx = self.Sxx[self.freqRange, :][0]

            # Plots Spectrogram
            self.axes.pcolormesh(
                self.time, self.freq, 10*np.log10(self.Sxx), cmap='inferno')
            self.axes.set_ylabel('Frequency [Hz]', color='white')
            self.axes.set_xlabel('Time [s]', color='white')
            self.axes.set_yscale('symlog')

            self.spectrogram_widget.draw()
            self.figure.canvas.draw()
    # Making a picture of the spectrogram to use it the pdf
            plt.savefig('Spectrogram.png')
