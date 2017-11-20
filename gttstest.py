from gtts import gTTS
import os
import time
import webbrowser

while True:
    bla = input()
    tts = gTTS(text=bla, lang='nl')
    tts.save(bla + ".mp3")

    webbrowser.open(bla + ".mp3")
    time.sleep(2)
    os.system("taskkill /im wmplayer.exe /f")
