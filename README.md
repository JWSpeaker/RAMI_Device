# RAMI_Device

#STT

Python 마이크 입력
pyaudio 설치
```
$ pip3 install pyaudio
```

Err
```

...

ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
```
해결법
```
//찾는중...
```


#TTS
오디오 출력을 위한 pygame 설치	//오디오 출력에 다른 모듈 사용 고려

unable to run sdl-config . please make sure a development version of sdl is installed 오류
```
$ sudo apt-get build-dep python-pygame
$ sudo apt-get install mercurial
$ pip3 install hg+http://bitbucket.org/pygame/pygame
```