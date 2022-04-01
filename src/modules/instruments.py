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
    def __init__(self):
        super().__init__()
        self.BASE_FREQ = 440
        self.PIANO_SAMPLING_RATE=44100
        self.octave_number =1  #default

    def key_freq(self,key_index,octave_number):

        n= self.n_jumps(key_index,octave_number)
        print('number of jumps:')
        print(n)
        print('octave:')
        print(octave_number)
        note_freq=self.BASE_FREQ*pow(2,n/12)
        print('freq:')
        print(note_freq)
        return note_freq

    def generating_wave(self,freq,duration=0.5):
        time = np.linspace(0, duration, int(self.PIANO_SAMPLING_RATE * duration))
        piano_wave = 0.6*np.sin(2 * np.pi * freq * time) * np.exp(-0.0015 * 2 * np.pi * freq * time)
        #overtones 
        piano_wave += 0.4*np.sin(2 * 2 * np.pi * freq * time) * np.exp(-0.0015 * 2 * np.pi * freq * time) / 2
       
        piano_wave += piano_wave * piano_wave * piano_wave
        #piano_wave *= 1 + 16 * time * np.exp(-6 * time)
        return  piano_wave
    
    def play_note(self,input_note):
         sd.play(input_note, self.PIANO_SAMPLING_RATE)
    def dial_value(self,dial_number):
        #TODO:LIMIT DIAL 1-7
        self.octave_number= dial_number
        print('HERE DIAL')
        print(self.octave_number)
    def n_jumps(self,key_index,octave_number):
        OCTAVE_LENGTH = 12
        A4_INDEX = 10

        if octave_number==0 :
            n= OCTAVE_LENGTH - key_index +12*3+9
            return -n
        elif octave_number==1:
            n= OCTAVE_LENGTH - key_index+12*2+9
            return -n
        elif octave_number==2:
            n= OCTAVE_LENGTH - key_index+12+9
            return -n
        elif octave_number==3:
            n= OCTAVE_LENGTH - key_index+9
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
        if key_index <12:
            octave_number= self.octave_number
        else:
            key_index= key_index - 12
            octave_number= self.octave_number+1
            
        freq= self.key_freq(key_index,octave_number)
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
