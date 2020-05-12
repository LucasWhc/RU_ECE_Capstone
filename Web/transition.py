import librosa
import librosa.display
import pylab
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
import numpy as np
from mido import Message, MidiFile, MidiTrack
from note_num import num

# mid = MidiFile()
# track = MidiTrack()


# file_path = '/Users/lucifer.w/Documents/Capstone/Web/resource/xiaoxingxing.wav'
# file_path = '/Users/lucifer.w/Documents/Capstone/Web/resource/test.wav'


def beat_length(time):
    time /= 60 * 1000
    time = 1 / time
    return time


# def one_note(note, time, before_note=0, vel=64, ins=2):
#     if type(note) == str:
#         note = num(note)
#     track.append(Message('program_change', channel=0, program=ins, time=0))
#     track.append(Message('note_on', note=note, velocity=vel, time=before_note, channel=0))
#     track.append(Message('note_off', note=note, velocity=vel, time=time, channel=0))
#
#
# def create_midi(note, beat, time, before_note, ins=2):
#     pig = int(beat_length(time))
#     if before_note is None:
#         x = len(beat)
#         for i in range(x):
#             if note[i] == 'null':
#                 if type(note[i]) == str:
#                     note[i] = num(note[i])
#                 track.append(Message('program_change', channel=0, program=ins, time=0))
#                 track.append(Message('note_on', note=note[i], velocity=0, time=before_note, channel=0))
#                 track.append(Message('note_off', note=note[i], velocity=0, time=beat[i] * pig, channel=0))
#                 # one_note(note[i], beat[i] * pig, vel=0, ins=ins)
#             else:
#                 if type(note[i]) == str:
#                     note[i] = num(note[i])
#                 track.append(Message('program_change', channel=0, program=ins, time=0))
#                 track.append(Message('note_on', note=note, velocity=64, time=before_note, channel=0))
#                 track.append(Message('note_off', note=note, velocity=64, time=beat[i] * pig, channel=0))
#                 # one_note(note[i], beat[i] * pig, ins=ins)
#     elif before_note and len(before_note) == 1:
#         x = len(beat)
#         for i in range(x):
#             if type(note[i]) == str:
#                 note[i] = num(note[i])
#             track.append(Message('program_change', channel=0, program=ins, time=0))
#             track.append(Message('note_on', note=note, velocity=64, time=before_note * pig, channel=0))
#             track.append(Message('note_off', note=note, velocity=64, time=beat[i] * pig, channel=0))
#             # one_note(note[i], beat[i] * pig, before_note * pig, ins=ins)
#     else:
#         x = len(beat)
#         for i in range(x):
#             if type(note[i]) == str:
#                 note[i] = num(note[i])
#             track.append(Message('program_change', channel=0, program=ins, time=0))
#             track.append(Message('note_on', note=note, velocity=64, time=before_note[i] * pig, channel=0))
#             track.append(Message('note_off', note=note, velocity=64, time=beat[i] * pig, channel=0))
#             # one_note(note[i], beat[i] * pig, before_note[i] * pig, ins=ins)


def transition(file_path, wh):
    mid = MidiFile()
    track = MidiTrack()
    np.set_printoptions(threshold=np.inf)
    x, sr = librosa.load(file_path, sr=16000)
    # sr/2(or size of x)*hop_length = size of one row in chromagram
    # hop_length=2000, fmin=200, fmax=1500, n_mels=200 for Little Star
    hop_length = 2000
    fmin = 200
    fmax = 1500
    n_mels = 200
    chromagram = librosa.feature.chroma_stft(x, sr=sr, hop_length=hop_length)
    # in chromagram, value == 1 means this pitch absolutely exist,
    # n_mels gives the stamps at y-axis of melspectrogram,
    # fmax and fmin gives the upper bound and lower bound of the frequncy
    melspectrogram = librosa.feature.melspectrogram(x, sr=sr, n_mels=n_mels, fmax=fmax, fmin=fmin)
    plt.figure(figsize=(10, 4))
    melspectrogram_db = librosa.power_to_db(melspectrogram, ref=np.max)
    librosa.display.specshow(melspectrogram_db, x_axis='time', y_axis='mel', sr=sr, fmax=fmax, fmin=fmin)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel-frequency spectrogram')
    plt.tight_layout()
    # plt.savefig("/Users/lucifer.w/Desktop/Results/spectrogram" + i + ".png")
    plt.savefig("/Users/lucifer.w/Desktop/Results/" + str(wh) + "/spectrogram" + str(wh) + ".png")
    plt.show()
    plt.figure(figsize=(15, 5))
    librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', hop_length=hop_length, cmap='coolwarm')
    # plt.savefig("/Users/lucifer.w/Desktop/Results/chromagram.png")
    plt.savefig("/Users/lucifer.w/Desktop/Results/" + str(wh) + "/chromagram" + str(wh) + ".png")
    plt.show()
    '''
    # data extract part
    sheet = [None] * np.size(chromagram[0, :])
    # access the data in these variables: variables[row,column]
    # get the size of a numpy array: np.size(array)
    row_C = chromagram[0, :]
    # print("row_C size is ")
    # print(np.size(row_C))
    # now, C_index is a tuple type value
    C_index = np.where(row_C == 1)
    # print(np.size(C_index))
    # print("In this part, the audio plays C: ")
    C = list(C_index)[0]
    # print(C)
    for m in C:
        sheet[m] = 'C'
    row_D = chromagram[2, :]
    # print("row_C size is ")
    # print(np.size(row_C))
    # now, C_index is a tuple type value
    D_index = np.where(row_D == 1)
    # print("In this part, the audio plays C: ")
    D = list(D_index)[0]
    for m in D:
        sheet[m] = 'D'
    row_E = chromagram[4, :]
    # print("row_C size is ")
    # print(np.size(row_C))
    # now, C_index is a tuple type value
    E_index = np.where(row_E == 1)
    # print("In this part, the audio plays C: ")
    E = list(E_index)[0]
    for m in E:
        sheet[m] = 'E'
    row_F = chromagram[5, :]
    # print("row_C size is ")
    # print(np.size(row_C))
    # now, C_index is a tuple type value
    F_index = np.where(row_F == 1)
    # print("In this part, the audio plays C: ")
    F = list(F_index)[0]
    for m in F:
        sheet[m] = 'F'
    row_G = chromagram[7, :]
    # print("row_C size is ")
    # print(np.size(row_C))
    # now, C_index is a tuple type value
    G_index = np.where(row_G == 1)
    # print("In this part, the audio plays C: ")
    G = list(G_index)[0]
    for m in G:
        sheet[m] = 'G'
    row_A = chromagram[9, :]
    # print("row_C size is ")
    # print(np.size(row_C))
    # now, C_index is a tuple type value
    A_index = np.where(row_A == 1)
    # print("In this part, the audio plays C: ")
    A = list(A_index)[0]
    for m in A:
        sheet[m] = 'A'
    row_B = chromagram[11, :]
    # print("row_C size is ")
    # print(np.size(row_C))
    # now, C_index is a tuple type value
    B_index = np.where(row_B == 1)
    # print("In this part, the audio plays C: ")
    B = list(B_index)[0]
    for m in B:
        sheet[m] = 'B'
    # ... dictionary may make the code easier
    finalSheet = []
    for m in range(0, len(sheet)):
        if m == 0: finalSheet.append(sheet[m])
        if m > 0:
            if sheet[m] != sheet[m - 1]: finalSheet.append(sheet[m])
    '''
    # X = librosa.stft(x)
    # Xdb = librosa.amplitude_to_db(abs(X))   # 把幅度转成分贝格式
    # plt.figure(figsize=(14, 5))
    # librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log', cmap='coolwarm')
    # plt.colorbar()
    # plt.show()

    # import numpy as np
    # import IPython.display as ipd
    # np.set_printoptions(threshold=np.inf)
    # sr = 22050 # sample rate
    # T = 5.0    # seconds
    # t = np.linspace(0, T, int(T*sr), endpoint=False) # time variable
    # x = 0.5*np.sin(2*np.pi*220*t)# pure sine wave at 220 Hz
    # ipd.Audio(x, rate=sr) # load a NumPy array
    # librosa.output.write_wav('123.wav', x, sr)

    # spectrogram extract

    # divide by time

    print("whole time length")
    print(np.size(melspectrogram_db[0, :]))
    numlist = []
    index = -999
    for i in range(0, np.size(melspectrogram_db[0, :])):
        cnt = 0
        for j in range(0, np.size(melspectrogram_db[:, 0])):
            if melspectrogram_db[j, i] < -75:
                break
            if melspectrogram_db[j, i] > -60:
                cnt = cnt + 1
                if cnt > np.size(melspectrogram_db[:, 0]) * 2 / 3:
                    break
        if cnt > np.size(melspectrogram_db[:, 0]) * 2 / 3:
            n = len(numlist)
            if index <= i - 5:
                numlist.append(i)
            index = i

    print("Divided by time:")
    print(numlist)

    # extract frequncy

    # print("The pitch of the note:")
    # print(finalSheet)

    sheetSimple = []
    sheetSimple1 = []
    # for i in range(1,len(numlist)+1):
    #     maxVol = -10000000000000000000
    #     maxindex = -1
    #     for j in range(0, np.size(melspectrogram_db[:, 0])):
    #         addVol = 0
    #         if i != len(numlist):
    #             for k in range(numlist[i-1], numlist[i]):
    #                 addVol += melspectrogram_db[j, k]
    #             if addVol > maxVol:
    #                 maxVol = addVol
    #                 maxindex = j
    #         else:
    #             for k in range(numlist[i-1], np.size(melspectrogram_db[0, :])):
    #                 addVol += melspectrogram_db[j, k]
    #             if addVol > maxVol:
    #                 maxVol = addVol
    #                 maxindex = j
    #     sheetSimple.append(maxindex)
    # print(sheetSimple)

    # use a 5-length window to calculate the max volumn then get the freq
    for i in range(0, len(numlist)):
        if i < len(numlist) - 1:
            target = numlist[i] + 5
        else:
            target = numlist[i]
        addVol = 0
        for k in range(0, 9):
            addVol += melspectrogram_db[k, target]
        maxvol = -1000000
        maxindex = -1
        for j in range(4, np.size(melspectrogram_db[:, 0]) - 5):
            # for k in range(j-2,j+3):
            #     addVol+=melspectrogram_db[k,target]
            if addVol > maxvol:
                maxvol = addVol
                maxindex = j
            addVol = addVol + melspectrogram_db[j + 5, target] - melspectrogram_db[j - 4, target]
        maxvol = -1000000
        for k in range(maxindex - 4, maxindex + 5):
            if melspectrogram_db[k, target] > maxvol:
                maxvol = melspectrogram_db[k, target]
                maxindex = k
        sheetSimple.append(maxindex)
        sheetSimple1.append(fmin + (maxindex) * (fmax - fmin) / n_mels)
    # print(sheetSimple)
    print("Frequency of note:")
    print(sheetSimple1)

    buildSheet = []
    c = 0
    dic = {"c4": 265.0, "c4#": 280.0, "d4": 291.0, "d4#": 317.0, "e4": 336.5, "f4": 356.0, "f4#": 375.5, "g4": 401.5,
           "a4": 453.5, "b4": 512.0, "c5": 544.0, "d5": 616.0, "e5": 700.0, "f5": 740.0, "g5": 830.0, "a5": 940.0,
           "b5": 1050.0, "c6": 1116.5, "d6": 1246.5, "e6": 1370.0, "f6": 1428.5}
    for i in sheetSimple1:
        c = 0
        for j in dic:
            if dic[j] - 10 < i < dic[j] + 10:
                c = 1
                buildSheet.append(j)
                break
        if c == 0:
            buildSheet.append("null")
    print("Final Note Sheet:")
    print(buildSheet)

    # create MIDI

    numlist.append(np.size(melspectrogram_db[0, :]))
    min = 10000000000
    for i in range(len(numlist) - 1):
        if numlist[i + 1] - numlist[i] < min:
            min = numlist[i + 1] - numlist[i]
    L = min
    beats = []
    for i in range(len(buildSheet)):
        beats.append(round((numlist[i + 1] - numlist[i]) / L))
    mid.tracks.append(track)
    # create_midi(buildSheet, beats, 250, None)
    # mid.save('xiaoxingxing2.mid')
    # mid.save('/Users/lucifer.w/Desktop/Results/MIDI' + str(i) + '.mid')
    # mid.save('/Users/lucifer.w/Desktop/' + str(wh) + '/MIDI' + str(wh) + '.mid')
    note = buildSheet
    beat = beats
    time = 250
    ins = 2
    before_note = None
    pig = int(beat_length(time))
    if before_note is None:
        x = len(beat)
        for i in range(x):
            if note[i] == 'null':
                if type(note[i]) == str:
                    note[i] = num(note[i])
                track.append(Message('program_change', channel=0, program=ins, time=0))
                track.append(Message('note_on', note=note[i], velocity=0, time=0, channel=0))
                track.append(Message('note_off', note=note[i], velocity=0, time=beat[i] * pig, channel=0))
                # one_note(note[i], beat[i] * pig, vel=0, ins=ins)
            else:
                if type(note[i]) == str:
                    note[i] = num(note[i])
                track.append(Message('program_change', channel=0, program=ins, time=0))
                track.append(Message('note_on', note=note[i], velocity=64, time=0, channel=0))
                track.append(Message('note_off', note=note[i], velocity=64, time=beat[i] * pig, channel=0))
                # one_note(note[i], beat[i] * pig, ins=ins)
    mid.save('/Users/lucifer.w/Desktop/Results/' + str(wh) + '/MIDI' + str(wh) + '.mid')
# transition(file_path)
