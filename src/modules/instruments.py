
import numpy as np
import pygame
import wave
from numpy import random
import app
from modules.utility import print_debug, print_log
from modules import interface

import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QShortcut, QLabel, QApplication


class Instrument():
    # super class of all instruments
    # should contain the common general functions
    def __init__(self):
        self.master_volume = 1

    def float_to_int16(self, float_array):
        int_array = np.int16(float_array * (32767/2))
        return int_array

    def play_sound(self, sound):

        sound = np.int16(np.multiply(sound, self.master_volume))
        sound_object = pygame.sndarray.make_sound(array=sound)
        sound_object.play()

    def set_volume(self, volume):
        self.master_volume = volume/100
    # Functions;
    # play notes
    # import base sample/tone
    # set and get the following
    # Variables
    # current tone
    # instrument name

# ahlan bel inhertiance


class Drums(Instrument):

    def __init__(self):
        super().__init__()
        self.drum_sampling_rate = 44100
        self.drum_kit_tones = {
            'snare': ['snare1.wav', 'snare2.wav', 'snare3.wav', 'snare4.wav'], 'hat': ['hat1.wav', 'hat2.wav', 'hat3.wav', 'hat4.wav'], 'kick': ['kick1.wav', 'kick2.wav', 'kick3.wav', 'kick4.wav'], 'FLoor_tom': ['Floor_tom1.wav', 'Floor_tom2.wav', 'Floor_tom3.wav', 'Floor_tom4.wav'], 'H_tom': ['H_tom1.wav', 'H_tom2.wav', 'H_tom3.wav', 'H_tom4.wav'], 'ride_cymbal': ['ride_cymbal1.wav', 'ride_cymbal2.wav', 'ride_cymbal3.wav', 'ride_cymbal4.wav'], 'crash_cymbal': ['crash_cymbal1.wav', 'crash_cymbal2.wav', 'crash_cymbal3.wav', 'crash_cymbal4.wav']}

        self.read_drum_tones = {
            'snare': [], 'hat': [], 'kick': [], 'FLoor_tom': [], 'H_tom': [], 'ride_cymbal': [], 'crash_cymbal': []}
        self.read_all_samples()

    def read_all_samples(self):
        for key in self.drum_kit_tones:
            for index in self.drum_kit_tones[key]:
                tone = wave.open('resources\drum_tones\\' + str(index))
                signal = tone.readframes(-1)
                signal = np.frombuffer(signal, dtype=np.int16)
                self.read_drum_tones[key].append(signal)

    def play_drums(self, tone):
        print_debug(tone)
        play_sound = np.int16(random.choice(self.read_drum_tones[tone]))
        self.play_sound(play_sound)

    def selecting_drum_kit(self, index):
        self.play_drums(index)

    def key_drums(self, key):

        if key == 's':
            self.play_drums("snare")
        elif key == 'k':
            self.play_drums("kick")
        elif key == 'h':
            self.play_drums("hat")
        elif key == 'f':
            self.play_drums("FLoor_tom")
        elif key == 't':
            self.play_drums("H_tom")
        elif key == 'r':
            self.play_drums("ride_cymbal")
        elif key == 'c':
            self.play_drums("crash_cymbal")


class Piano(Instrument):
    def __init__(self):
        super().__init__()
        self.BASE_FREQ = 440
        self.PIANO_SAMPLING_RATE = 44100
        self.octave_number = 1  # default
        self.sus_value = 1
        self.overtone_value = 1

    def key_freq(self, key_index, octave_number):

        n = self.n_jumps(key_index, octave_number)
        print_debug('number of jumps:')
        print_debug(n)
        print_debug('octave:')
        print_debug(octave_number)
        note_freq = self.BASE_FREQ*pow(2, n/12)
        print_debug('freq:')
        print_debug(note_freq)
        return note_freq

    def alter_sus_overtones_values(self, sus, overtones):
        self.sus_value = sus
        self.overtone_value = overtones

    def generating_wave(self, freq, duration=2.5):
        time = np.linspace(0, duration, int(
            self.PIANO_SAMPLING_RATE * duration))
        piano_wave = 0.6*np.sin(2 * np.pi * freq * time) * \
            np.exp(-0.0015 * self.sus_value * 2 * np.pi * freq * time)
        # overtones
        piano_wave += 0.4*np.sin(2 * 2 * np.pi * freq * time) * \
            np.exp(-0.0015 * self.overtone_value * 2 * np.pi * freq * time) / 2

        piano_wave += piano_wave * piano_wave * piano_wave
        # piano_wave *= 1 + 16 * time * np.exp(-6 * time)

        piano_wave = self.float_to_int16(piano_wave)
        return piano_wave

    def play_note(self, input_note):

        print_debug(input_note)
        sound_object = pygame.sndarray.make_sound(array=input_note)
        sound_object.play()

    def key_piano(self, key):
        self.generating_note(interface.piano_key_index_dict[key])
        print_debug("num sound channels " + str(pygame.mixer.get_num_channels()))

    def dial_value(self, dial_number):
        # TODO:LIMIT DIAL 1-7
        self.octave_number=dial_number

    def n_jumps(self, key_index, octave_number):
        OCTAVE_LENGTH=12
        A4_INDEX=10

        if octave_number == 0:
            n=OCTAVE_LENGTH - key_index + 12*3+9
            return -n
        elif octave_number == 1:
            n=OCTAVE_LENGTH - key_index+12*2+9
            return -n
        elif octave_number == 2:
            n=OCTAVE_LENGTH - key_index+12+9
            return -n
        elif octave_number == 3:
            n=OCTAVE_LENGTH - key_index+9
            return -n
        elif octave_number == 4:
            n=key_index-A4_INDEX + 1
            return n

        elif octave_number == 5:
            n=key_index+3
            return n
        elif octave_number == 6:
            n=key_index+12+3
            return n
        elif octave_number == 7:
            n=key_index+12*2+3
            return n
        elif octave_number == 8:
            n=key_index+12*3+3
            return n

    def generating_note(self, key_index):
        if key_index < 12:
            octave_number=self.octave_number
        else:
            key_index=key_index - 12
            octave_number=self.octave_number+1

        freq=self.key_freq(key_index, octave_number)
        wave=self.generating_wave(freq, duration=3)

        self.play_sound(wave)


class Guitar(Instrument):
    def __init__(self):
        super().__init__()

        self.GUITAR_SAMPLING_RATE=44100
        self.guitar_chords={
            'G_major': [98, 123, 147, 196, 247, 392],
            'D_major': [82, 110, 147, 220, 294, 370],
            'C_major': [82, 131, 165, 196, 262, 329],
            'E_major': [82, 123, 165, 208, 247, 329],
            'A_major': [82, 110, 165, 220, 277, 329]}
        self.chord=self.guitar_chords['G_major']  # default
        self.samples=[]

    def wavetable_initiator(self, string_pitch):
        """Generates a new wavetable for the string."""

        print_debug(string_pitch)
        wavetable_size=self.GUITAR_SAMPLING_RATE // int(string_pitch)
        wavetable=(2 * np.random.randint(0, 2,
                     wavetable_size) - 1).astype(np.float)
        return wavetable

    def get_sample(self, wavetable, n_samples):
        """Synthesizes a new waveform from an existing wavetable, modifies last sample by averaging."""
        current_sample=0
        previous_value=0
        samples=[]
        while len(samples) < n_samples:
            wavetable[current_sample]=0.5 * \
                (wavetable[current_sample] + previous_value)
            samples.append(wavetable[current_sample])
            previous_value=samples[-1]
            current_sample += 1
            current_sample=current_sample % wavetable.size
        return np.array(samples)

    def guitar_chord_selection(self, dial_number):
        if dial_number == 1:
            self.chord=self.guitar_chords['G_major']
        elif dial_number == 2:
            self.chord=self.guitar_chords['D_major']
        elif dial_number == 3:
            self.chord=self.guitar_chords['C_major']
        elif dial_number == 4:
            self.chord=self.guitar_chords['E_major']
        elif dial_number == 5:
            self.chord=self.guitar_chords['A_major']

    def guitar_chord_selection(self, dial_number):

        self.chord_number=self.guitar_chords['D_major']

    def play_string(self, sound):
        sound=self.float_to_int16(sound)
        self.play_sound(sound)

    def guitar_string_sound(self, string_num):
        print_debug('chord:')
        print_debug(self.chord)
        pitchs=self.chord
        print_debug('freq:')
        print_debug(pitchs[string_num])
        # frequancy is the frequancy of string in the chosen chord
        frequancy=pitchs[string_num]
        print_debug('freq entering the equation:')
        print_debug(frequancy)
        wave=self.wavetable_initiator(frequancy)
        guitar_sound=self.get_sample(wave, self.GUITAR_SAMPLING_RATE * 5)
        self.play_string(guitar_sound)

    def set_chord_lcd(self, lcd):
        if lcd == 0:
            return "o"
        elif lcd == 1:
            return 'g'
        elif lcd == 2:
            return 'D'
        elif lcd == 3:
            return 'C'
        elif lcd == 4:
            return 'E'
        elif lcd == 5:
            return 'A'

    def key_guitar(self, key):

        if key == '1':
            self.guitar_string_sound(0)
        elif key == '2':
            self.guitar_string_sound(1)
        elif key == '3':
            self.guitar_string_sound(2)
        elif key == '4':
            self.guitar_string_sound(3)
        elif key == '5':
            self.guitar_string_sound(4)
        elif key == '6':
            self.guitar_string_sound(5)
