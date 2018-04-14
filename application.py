from tts.tts import TTS, PlayVoice
from stt.stt_request import Record, Speech2Text

if __name__ == "__main__":
    Record("output.wav")
    TTS(Speech2Text("output.wav"))
    PlayVoice()
