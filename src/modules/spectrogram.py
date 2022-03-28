#should contain old spectrogram code modified to work with the new classes

#OLD FUNCTIONS 


    def CreateSpectrogramFigure(self):
        self.figure = plt.figure()                     # Create matplotlib fig
        self.figure.patch.set_facecolor('black')
        self.axes = self.figure.add_subplot()
        self.Spectrogram = Canvas(self.figure)
        self.SpectrogramBox_2.addWidget(self.Spectrogram)

    def plotSpectro(self):

        #Clear spectrogram before plotting
        self.Spectrogram.draw()
        self.figure.canvas.draw()

        FS = 250

        # Corner Case Of Empty Channel
        if len(self.ChannelLineArr[classes.SpectroSelectedIndex].Amplitude) == 0:
            self.axes.clear()
            self.Spectrogram.draw()
            self.figure.canvas.draw()

        else:
            if self.fsampling != 1:
                FS = self.fsampling

            self.SignalArray = np.array(
                self.ChannelLineArr[classes.SpectroSelectedIndex].Amplitude)
            self.freq, self.time, self.Sxx = signal.spectrogram(
                self.SignalArray, fs=FS, window='hanning', nperseg=128, noverlap=64, detrend=False, mode='magnitude', scaling='density')

            self.max_freq = np.max(self.freq)
            self.axes.set_ylim([0, self.max_freq])

            # Slices freq arr into range specified by sliders
            self.freqRange = np.where((self.freq >= classes.FreqRangeMin) & (
                self.freq <= classes.FreqRangeMax))
            self.freq = self.freq[self.freqRange]
            self.Sxx = self.Sxx[self.freqRange, :][0]

            # Plots Spectrogram
            self.axes.pcolormesh(
                self.time, self.freq, 10*np.log10(self.Sxx), cmap=classes.SpectroTheme)
            self.axes.set_ylabel('Frequency [Hz]', color='white')
            self.axes.set_xlabel('Time [s]', color='white')
            self.axes.set_yscale('symlog')

            self.Spectrogram.draw()
            self.figure.canvas.draw()
# Making a picture of the spectrogram to use it the pdf
            plt.savefig('Spectrogram.png')

    def SetSpectroSelectedIndex(self, Input):
        classes.SpectroSelectedIndex = Input
        self.plotSpectro()

    def SetSpectroTheme(self, Input):
        classes.SpectroTheme = Input
        self.plotSpectro()

    def SpectrogramFrequency(self, Input, MinOrMax):
        if MinOrMax == "min":
            if Input < classes.FreqRangeMax:
                classes.FreqRangeMin = Input
            else:
                # Prevents min from exceeding max
                self.MinRangeSlider.setValue(classes.FreqRangeMin)
        if MinOrMax == "max":
            if Input > classes.FreqRangeMin:
                classes.FreqRangeMax = Input
            else:
                # Prevents max from going below min
                self.MaxRangeSlider.setValue(classes.FreqRangeMax)

        self.plotSpectro()
        util.printDebug(MinOrMax + "SpectroSlider: " + str(Input))

