import subprocess
import pygame

def RecordAudio(file_name):
    subprocess.run('arecord -D "plughw:1,0" -f S16_LE -t wav -r 16000 -d 4 > ' + file_name, shell = True)




#mp3 재생하기위해 pygame 썼음
def PlayAudio(file_name):
    pygame.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    #재생되는 동안 대기
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
