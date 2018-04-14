"""

"""
import requests
import subprocess

def Record(file_name):
    res = subprocess.run('arecord -D "plughw:1,0" -f S16_LE -t wav -r 16000 -d 4 > ' + file_name, shell = True)


def Speech2Text(file_name):

    f = open(file_name, 'rb')
    wav = f.read()

    url = "https://www.google.com/speech-api/v2/recognize?output-json&lang=ko&key="
    key = "AIzaSyAYncl6rUXdQwAv5j_AHz8hdqcBlQIdEDk"
    headers = {
        "content-type" : "audio/l16;rate=16000"
    }
    res = requests.post(url + key, headers = headers, data = wav)
    result = res.text
    text = result[result.find("\":\"")+3: result.find("\",\"")]
    print(text)
    return text;



#module test code
if __name__ == "__main__":
    print('main')
    #res = subprocess.run('arecord -D "plughw:1,0" -f S16_LE -t wav -r 16000 -d 4 > ouput.wav', shell = True)
