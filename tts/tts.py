import os
import sys
import urllib.request
import pygame
import time

#naver developer API
client_id = "H7tbSw0Zq64yn8mgcMv6"
client_secret = "4I96Qv4clY"

url = "https://openapi.naver.com/v1/voice/tts.bin"

def TTS(text):
    """
    주석
    """

    encText = urllib.parse.quote(str(text))
    data = "speaker=mijin&speed=0&text=" + encText;

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if(rescode==200):
        print('text : ', text)
        response_body = response.read()
        with open('result_voice.mp3', 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)

def PlayVoice():
    print('PlayVoice Call')
    pygame.init()
    pygame.mixer.music.load('result_voice.mp3')
    pygame.mixer.music.play()
    #재생되는 동안 대기
    time.sleep(10)

def main():
    TTS("안녕하세요. 오늘의 날씨는 영상 10도이며 미세먼지 농도는 나쁨입니다. 강수확률은 60%이고 눈이 예상됩니다. 이상입니다.")
    PlayVoice()

if __name__ == "__main__":
    main()
