from tts.tts import TTS
from stt.stt_request import Speech2Text
from audio.audio import PlayAudio, RecordAudio

file_name = "./data/output.wav"

def main():
    while True:
        RecordAudio(file_name)






if __name__ == "__main__":
    file_name = "./data/output.wav"
    RecordAudio(file_name)
    TTS(Speech2Text(file_name))
    PlayAudio()
