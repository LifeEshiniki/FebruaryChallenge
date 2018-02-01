import pretty_midi

#Midiファイルの読み込み
midi_data = pretty_midi.PrettyMIDI('test.mid')

#ドラム以外の楽器の音を半音上げる
for instrument in midi_data.instruments:
    if not instrument.is_drum:
        for note in instrument.notes:
            note.pitch += 1
#このデータを新たなmidiファイルに書き込み
midi_data.write("pitch_up_test.mid")
import pretty_midi

#midiファイルの生成
cello_c_chord = pretty_midi.PrettyMIDI()
#チェロの音色で
cello_program = pretty_midi.instrument_name_to_program('Cello')
cello = pretty_midi.Instrument(program=cello_program)
# ド・ミ・ソの和音
for note_name in ['C5', 'E5', 'G5']:
    note_number = pretty_midi.note_name_to_number(note_name)
    #ヴェロシティ（音量）を100、0.5秒間鳴らす
    note = pretty_midi.Note(
        velocity=100, pitch=note_number, start=0, end=.5)
    cello.notes.append(note)
cello_c_chord.instruments.append(cello)
#cello-C-chord.midというファイルを生成
cello_c_chord.write('cello-C-chord.mid')
