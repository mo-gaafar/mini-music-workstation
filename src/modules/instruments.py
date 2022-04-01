#TODO: structure needs more work
from types import new_class
import numpy as np
import sounddevice as sd
class Instrument():
    # super class of all instruments
    # should contain the common general functions
    def __init__(self):
        pass
    # Functions;
    # play notes
    # import base sample/tone
    # set and get the following
    # Variables
    # current tone
    # instrument name

# ahlan bel inhertiance


class Piano(Instrument):
    octave_label_dict={0:['A', 'A#', 'B']
                ,1:['C', 'C#', 'D','D#','E','F','F#','G', 'G#','A', 'A#', 'B']
                ,2:['C', 'C#', 'D','D#','E','F','F#','G', 'G#','A', 'A#', 'B']
                ,3:['C', 'C#', 'D','D#','E','F','F#','G', 'G#','A', 'A#', 'B']
                ,4:['C', 'C#', 'D','D#','E','F','F#','G', 'G#','A', 'A#', 'B']
                ,5:['C', 'C#', 'D','D#','E','F','F#','G', 'G#','A', 'A#', 'B']
                ,6:['C', 'C#', 'D','D#','E','F','F#','G', 'G#','A', 'A#', 'B']
                ,7:['C', 'C#', 'D','D#','E','F','F#','G', 'G#','A', 'A#', 'B']
                ,8:['C']}
    def __init__(self):
        super().__init__()
        self.BASE_FREQ = 440
        self.PIANO_SAMPLING_RATE=44100
        self.octave_number =6  #default

    def key_freq(self,key_index):

        n= self.n_jumps(key_index)
        print(n)
        note_freq=self.BASE_FREQ*pow(2,n/12)
        return note_freq

    def generating_wave(self,freq,duration=0.5):
        time = np.linspace(0, duration, int(self.PIANO_SAMPLING_RATE * duration))
        piano_wave =0.6*np.sin(2 * np.pi * freq * time) * np.exp(-0.0004 * 2 * np.pi * freq * time)
        #overtones 
        piano_wave += np.sin(2 * 2 * np.pi * freq * time) * np.exp(-0.0004 * 2 * np.pi * freq * time) / 2
        piano_wave += np.sin(3 * 2 * np.pi * freq * time) * np.exp(-0.0004 * 2 * np.pi * freq * time) / 4
        piano_wave += np.sin(4 * 2 * np.pi * freq * time) * np.exp(-0.0004 * 2 * np.pi * freq * time) / 8
        piano_wave += np.sin(5 * 2 * np.pi * freq * time) * np.exp(-0.0004 * 2 * np.pi * freq * time) / 16
        piano_wave += np.sin(6 * 2 * np.pi * freq * time) * np.exp(-0.0004 * 2 * np.pi * freq * time) / 32
        piano_wave += piano_wave * piano_wave * piano_wave
        #piano_wave *= 1 + 16 * time * np.exp(-6 * time)
        return  piano_wave
    
    def play_note(self,input_note):
         sd.play(input_note, 0.5*self.PIANO_SAMPLING_RATE)
    def n_jumps(self,key_index):
        OCTAVE_LENGTH = 12
        A4_INDEX = 10
        #i= the octave number
        #index is the button pressed
        octave_number = self.octave_number
        if octave_number==0 :
            n= OCTAVE_LENGTH - key_index +12*3+10
            return -n
        elif octave_number==1:
            n= OCTAVE_LENGTH - key_index+12*2+10
            return -n
        elif octave_number==2:
            n= OCTAVE_LENGTH - key_index+12+10
            return -n
        elif octave_number==3:
            n= OCTAVE_LENGTH - key_index+10
            return -n
        elif octave_number== 4:
            n= key_index-A4_INDEX +1
            return n

        elif octave_number== 5:
            n=key_index+3
            return n
        elif octave_number== 6:
            n=key_index+12+3
            return n
        elif octave_number== 7:
            n=key_index+12*2+3
            return n
        elif octave_number== 8:
            n=key_index+12*3+3
            return n
    def generating_note(self,key_index):
        freq= self.key_freq(key_index)
        wave= self.generating_wave(freq,duration=0.5)
        self.play_note(wave)
    
#TODO: make this adaptable to the 3 instrument types
#TODO: connect in interface
def keyboard_pressed(key, instrument_index):
    # match key: match case needs python 3.10...
    #     case 'a':
    #         pass
    #     case  #TODO: do this in the future :(

    if key == 'a':
        pass
    elif key == 's':
        pass
    elif key == 'd':
        pass
    elif key == 'f':
        pass
    elif key == 'g':
        pass
    elif key == 'h':
        pass
