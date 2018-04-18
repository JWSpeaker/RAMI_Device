from tts.tts import TTS
from stt.stt_request import Speech2Text
from audio.audio import RecordAudio
from BayesianFilter.module import Predict
from Command.action import Action

file_name = "./data/output.wav"

def main():
    while True:
        RecordAudio(file_name)
        text = Speech2Text(file_name)
        print('text : ' + text)
        #text = input('input >>')
        if text :
            command = Predict(text)
            print('command : ' + command)
            result = Action(command)
            print('result : ' + result)
            if result == 'exit':
                exit_coment = '종료하겠습니다. 감사합니다.'
                print(exit_coment)
                TTS(exit_coment)
                break;
            TTS(result)
        else:
            print('command is none')


if __name__ == "__main__":
    main()
    print('Program exit')

    #file_name = "./data/output.wav"
    #RecordAudio(file_name)
    #TTS(Speech2Text(file_name))
