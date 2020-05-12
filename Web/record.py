import pyaudio
import wave

# input_file_name = "input6.wav"
# input_file_name = "audio.wav"
# input_file_path = "/Users/lucifer.w/Desktop/Web/resource/"
# input_path = input_file_path + input_file_name


def get_audio(filepath):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    # RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = filepath
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    with open('/Users/lucifer.w/Desktop/Web/resource/set.txt', 'w+') as f:
        f.seek(0)
        f.truncate()
    print("*" * 10, "Start recording")
    frames = []
    while True:
        with open('/Users/lucifer.w/Desktop/Web/resource/set.txt', 'r') as f:
            lines = f.readlines()
            if len(lines) > 0:
                line = lines[0]
                if line == 'q':
                    break
        for i in range(0, int(RATE / CHUNK)):
            data = stream.read(CHUNK)
            frames.append(data)
            print('aa')
    # flag = False
    # temp = input('Press any key plus enter to stop:')
    # while not flag:
    #     if temp == '':
    #         for i in range(0, int(RATE / CHUNK)):
    #             data = stream.read(CHUNK)
    #             frames.append(data)
    #     else:
    #         flag = True
    print("*" * 10, "End\n")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    exit()
