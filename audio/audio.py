import subprocess

def RecordAudio(file_name):
    subprocess.run('arecord -D "plughw:1,0" -f S16_LE -t wav -r 16000 -d 4 > ' + file_name, shell = True)




def PlayAudio(file_name):
    subprocess.run('aplay ' + file_name)


"""
def PlayVoice():
    print('PlayVoice Call')
    pygame.init()
    pygame.mixer.music.load('result_voice.mp3')
    pygame.mixer.music.play()
    #재생되는 동안 대기
    time.sleep(5)
"""
