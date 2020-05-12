from flask import Flask, render_template, request
from record import get_audio
from terminate import terminate
from transition import transition
import os

app = Flask(__name__)

# input_file_name = "audio.wav"
# input_file_path = "/Users/lucifer.w/Desktop/Results/"
# input_path = input_file_path + input_file_name
# input_file_name = "audio.wav"
input_file_path = "/Users/lucifer.w/Desktop/Results/"
# input_path = input_file_path + input_file_name
i = 0


@app.route('/record', methods=['GET'])
def record():
    global i
    os.mkdir(input_file_path + str(i))
    get_audio(input_file_path + str(i) + '/audio' + str(i) + '.wav')
    return "recordend"


@app.route('/stop', methods=['GET'])
def stop():
    terminate()
    return "stopend"


@app.route('/trans', methods=['GET'])
def tran():
    global i
    transition(input_file_path + str(i) + '/audio' + str(i) + '.wav', i)
    i += 1
    # "/Users/sf/Desktop/RU/Capstone/SourceCode/Web/resource/xiaoxingxing.wav"
    return "transend"


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
