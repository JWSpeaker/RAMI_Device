from tts.tts import TTS
from stt.stt_request import Speech2Text
from audio.audio import RecordAudio
from BayesianFilter.module import Predict
from Command.action import Action

file_name = "./data/output.wav"

def main():
    while True:
        #RecordAudio(file_name)
        #command = Speech2Text(file_name)
        command = input('input >>')
        if command :
            print('command : ' + command)
            print('action : ' + Action(command))
            Predict(command)
        else:
            print('command is none')


if __name__ == "__main__":
    main()

    #file_name = "./data/output.wav"
    #RecordAudio(file_name)
    #TTS(Speech2Text(file_name))
