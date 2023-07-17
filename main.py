from music21 import *
import random

## Stochastic weights


random_note = random.choices(range(-2, 2), k=1)
start_note = random_note[0]
melody = []
midi_numbers = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]




markov_model = {
    0: {0: 0.2, 1: 0.2, 2: 0.2, -1: 0.2, -2: 0.2},
    1: {0: 0.2, 1: 0.2, 2: 0.2, -1: 0.2, -2: 0.2},
    -1: {0: 0.2, 1: 0.2, 2: 0.2, -1: 0.2, -2: 0.2},
    2: {0: 0.2, 1: 0.2, 2: 0.2, -1: 0.2, -2: 0.2},
    -2: {0: 0.2, 1: 0.2, 2: 0.2, -1: 0.2, -2: 0.2}
}


def generate_melody(markov_model, limit=3, start=start_note):
    n = 0
    curr_state = start
    next_state = None
    melody.append(curr_state)

    while n<limit:
        sequence = list(markov_model[curr_state].keys())
        weights = list(markov_model[curr_state].values())
        next_state = random.choices(sequence, weights)
        curr_state = next_state[0]
        melody.append(curr_state)
        n+=1
    # print(melody)
    return melody

generate_melody(markov_model)



def generate_random_midi_note (midi = midi_numbers):
    random_midi = random.choices(range(48, 59), k=1)
    # print(random_midi)
    return random_midi



def map_melody():
    random_midi_note = generate_random_midi_note()
    melody = generate_melody(markov_model)
    starting_note = pitch.Pitch(random_midi_note)

    
    note3 = note.Note(50)
    midi_melody = stream.Stream()
    midi_melody.append(note3)

    print(midi_melody)

    midi_melody.show()

    # print(starting_note.midi)
    
    # for x in melody:
    #     midi_melody.append(starting_note.transpose(x))      
    #     print(midi_melody)


    return

map_melody()