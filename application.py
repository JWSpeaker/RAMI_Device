from tts.tts import TTS
from stt.stt_request import Speech2Text
from audio.audio import RecordAudio

file_name = "./data/output.wav"

def main():
    while True:
        RecordAudio(file_name)
        command = Speech2Text(file_name)
        if command :
            print('command : ' + command)
        else:
            print('command is none')




if __name__ == "__main__":
    file_name = "./data/output.wav"
    RecordAudio(file_name)
    TTS(Speech2Text(file_name))
