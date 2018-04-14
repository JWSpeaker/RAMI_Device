from tts.tts import TTS
from stt.stt_request import Speech2Text
from audio.audio import PlayAudio, RecordAudio

if __name__ == "__main__":
    file_name = "./data/output.wav"
    RecordAudio(file_name)
    TTS(Speech2Text(file_name))
    PlayVoice('./data/result_voice.mp3')
