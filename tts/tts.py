import os
import sys
import urllib.request
import pygame

#naver developer API
client_id = "H7tbSw0Zq64yn8mgcMv6"
client_secret = "4I96Qv4clY"

url = "https://openapi.naver.com/v1/voice/tts.bin"

def TTS(text):
    """
    NAVER API
    @ref : https://developers.naver.com/docs/clova/api/CSS/API_Guide.md#RequestParameter
    """
    encText = urllib.parse.quote(str(text))
    data = "speaker=jinho&speed=0&text=" + encText;

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if(rescode==200):
        #print('text : ', text)
        response_body = response.read()
        with open('./data/result_voice.mp3', 'wb') as f:
            f.write(response_body)

        PlayAudio('./data/result_voice.mp3')
    else:
        print("Error Code:" + rescode)

#mp3 재생하기위해 pygame 썼음
def PlayAudio(file_name):
    pygame.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    #재생되는 동안 대기
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


#test code
if __name__ == "__main__":
    TTS("안녕하세요. 오늘의 날씨는 영상 10도이며 미세먼지 농도는 나쁨입니다. 강수확률은 60%이고 눈이 예상됩니다. 이상입니다.")
    PlayAudio('./data/result_voice.mp3')
