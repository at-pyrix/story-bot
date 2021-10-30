import os
import pyttsx3
import shutil
import random
from pydub import AudioSegment

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


os.chdir('Scripts')
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
    songs_list = ['Music\\Happy-Music-1.wav', 'Music\\Happy-Music-2.wav',
                  'Music\\Happy-Music-3.wav']
else:
    songs_list = ["Music\\Happy1.wav",
                  "Music\\Happy2.wav", "Music\\Happy3.wav"]


bgm = random.choice(songs_list)

print(f"Background Music: {bgm}")

bgm = AudioSegment.from_wav(bgm)

lower = bgm - 22

overlay = sound.overlay(lower, position=0)

os.chdir(default)
file_handle = overlay.export("Podcast.wav", format="wav")

shutil.rmtree('Cache')

print("\u001B[32m"+"Podcast Generated Successfully"+'\u001B[0m')
