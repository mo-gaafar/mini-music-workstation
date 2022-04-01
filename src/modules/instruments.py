#TODO: structure needs more work
from types import new_class


class Instrument():
    # super class of all instruments
    # should contain the common general functions
    def __init__(self):
        self.test
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
        piano_sampling_rate=44100

    def play_note(input_note):
         sd.play(input_note, piano_sampling_rate)
    def generating_note(self,octave_dect(i[index])):
        frequency= key_freq(octave_dect(i[index]))
        wave= generating_wave(freq,duration=0.5)
        play_note(wave)
    def key_freq(self,octave_dect(i[index])):
        n= n_jumps(self,octave_dect(i[index]))
        note_freq=base_freq*2^(n/12)
      return note_freq

    def generating_wave(self,freq,duration=0.5):
         time = np.linspace(0, duration, int(piano_sampling_rate * duration))
        piano_wave = np.sin(2 * np.pi * freq * time) * np.exp(-0.0004 * 2 * np.pi * freq * time)
        #overtones 
        piano_wave += np.sin(2 * 2 * np.pi * freq * time) * np.exp(-0.0004 * 2 * np.pi * freq * time) / 2
        piano_wave += np.sin(3 * 2 * np.pi * freq * time) * np.exp(-0.0004 * 2 * np.pi * freq * time) / 4
        piano_wave += np.sin(4 * 2 * np.pi * freq * time) * np.exp(-0.0004 * 2 * np.pi * freq * time) / 8
        piano_wave += np.sin(5 * 2 * np.pi * freq * time) * np.exp(-0.0004 * 2 * np.pi * freq * time) / 16
        piano_wave += np.sin(6 * 2 * np.pi * freq * time) * np.exp(-0.0004 * 2 * np.pi * freq * time) / 32
        piano_wave += piano_wave * piano_wave * piano_wave
        #piano_wave *= 1 + 16 * time * np.exp(-6 * time)
        return  piano_wave
    def n_jumps(self,octave_number,index):
        OCTAVE_LENGTH = 12
        A4_INDEX = 7
        #i= the octave number
        #index is the button pressed
        if octave_number==0 :
            n= OCTAVE_LENGTH - index +12^3+10
            return -n
        elif octave_number==1:
            n= OCTAVE_LENGTH - index+12^2+10
            return -n
        elif octave_number==2:
            n= OCTAVE_LENGTH - index+12+10
            return -n
        elif octave_number==3:
            n= OCTAVE_LENGTH - index+10
            return -n
        elif octave_number== 4:
            n= index-A4_INDEX 
            return -n
        elif i== 5:
            n=octave_dect(octave_number[index])+2
            return n
        elif i== 6:
            n=octave_dect(i[index])+12+2
            return n
        elif i== 7:
            n=octave_dect(i[index])+12^2+2
            return n
        elif i== 8:
            n=octave_dect(i[index])+12^3+2
            return n
    
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
