import random
import shutil
import pyttsx3
import os
from threading import Thread
from itertools import cycle
from time import time, sleep
from sys import stdout
from pydub import AudioSegment

done = False
error = False

start = time()

def animate(message):
    for c in cycle([f'⡿ {message}', f'⣟ {message}', f'⣯ {message}', f'⣷ {message}', f'⣾ {message}', f'⣽ {message}', f'⣻ {message}', f'⢿ {message}']):
        if error:
            print(f'\r\u001B[31m'+"An error Occurred"+"\u001B[0m")
            break
        if done:
            print(f'\r\u001B[32m\r✔️  Podcast Successfully Generated \u001B[33m{str (round(time() - start, 2))}s \u001B[0m \r')
            break

        stdout.write('\r' + '\u001B[36m' + c)
        stdout.flush()
        sleep(0.06)


Thread(target=animate, args=('Generating Podcast...',)).start()


engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 185)
voice = engine.getProperty("voices")

default = os.getcwd()


try:
    os.mkdir('Cache')
except FileExistsError:
    shutil.rmtree('Cache')
    os.mkdir('Cache')


def tts(audio, fileName, voice_id=0):
    if voice_id == -1:
        engine.setProperty('rate', 165)
    engine.setProperty('voice', voice[voice_id].id)
    engine.save_to_file(filename=fileName+".wav", text=audio)
    engine.runAndWait()


try:
    os.chdir('Scripts')
except Exception:
    error = True
    print("\r\u001B[33m"+"Run Script_Generator.py First"+"\u001B[0m")
    exit()
scripts = ["Host_Line_1", "Author_Line_1",
           "Host_Line_2", "Author_Story", "Host_Ending"]

for script in scripts:
    with open(f"{script}.txt", 'r', encoding='utf-8') as file:
        globals()[script] = file.read()
        file.close()

with open('theme.txt', 'r') as file:
    STORY = file.read()
    file.close()

os.chdir(default)
os.chdir('Cache')
tts(Host_Line_1, 'Host_Line_1', -1)
tts(Author_Line_1, 'Author_Line_1')
tts(Host_Line_2, 'Host_Line_2', -1)
tts(Author_Story, 'Author_Story')
tts(Host_Ending, 'Host_Ending', -1)


sound1 = AudioSegment.from_file(f"Host_Line_1.wav", format="wav")
sound2 = AudioSegment.from_file(f"Author_Line_1.wav", format="wav")
sound3 = AudioSegment.from_file(f"Host_Line_2.wav", format="wav")
sound4 = AudioSegment.from_file(f"Author_Story.wav", format="wav")
sound5 = AudioSegment.from_file(f"Host_Ending.wav", format="wav")

combined = sound1 + sound2 + sound3 + sound4 + sound5

os.chdir(default)
file_handle = combined.export("Podcast.wav", format="wav")
sound = AudioSegment.from_file('Podcast.wav')
songs_list = []

if STORY == "HAPPY":
    songs_list = os.listdir('Music\\Happy-Music')
    os.chdir('Music\\Happy-Music')
else:
    songs_list = os.listdir('Music\\Sad-Music')
    os.chdir('Music\\Sad-Music')


bgm = random.choice(songs_list)
bgm_segment = AudioSegment.from_wav(bgm)
lower = bgm_segment - 22

overlay = sound.overlay(lower, position=0)

os.chdir(default)
file_handle = overlay.export("Podcast.wav", format="wav")

shutil.rmtree('Cache')


done = True

print("\u001B[0m\nBackground Music: \u001B[33m"+bgm+"\u001b[0m")
